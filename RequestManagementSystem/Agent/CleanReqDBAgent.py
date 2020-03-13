########################################################################
# $HeadURL $
# File: CleanReqDBAgent.py
# Author: Krzysztof.Ciba@NOSPAMgmail.com
# Date: 2013/05/17 08:31:26
########################################################################
""" :mod: CleanReqDBAgent

    =====================

    .. module: CleanReqDBAgent

    :synopsis: cleaning RequestDB from obsolete records and kicking assigned requests

    .. moduleauthor:: Krzysztof.Ciba@NOSPAMgmail.com

    cleaning ReqDB from obsolete records and kicking assigned requests
"""
__RCSID__ = "$Id: $"
# #
# @file CleanReqDBAgent.py
# @author Krzysztof.Ciba@NOSPAMgmail.com
# @date 2013/05/17 08:32:08
# @brief Definition of CleanReqDBAgent class.

# # imports
import datetime
# # from DIRAC
from DIRAC import S_OK
from DIRAC.FrameworkSystem.Client.MonitoringClient import gMonitor
from DIRAC.Core.Base.AgentModule import AgentModule
from DIRAC.RequestManagementSystem.Client.ReqClient import ReqClient
from DIRAC.RequestManagementSystem.Client.Request import Request

AGENT_NAME = "RequestManagement/CleanReqDBAgent"

########################################################################
class CleanReqDBAgent( AgentModule ):
  """
  .. class:: CleanReqDBAgent

  """
  # # DEL GRACE PERIOD in DAYS
  DEL_GRACE_DAYS = 60
  # # DEL LIMIT
  DEL_LIMIT = 100
  # # KICK PERIOD in HOURS
  KICK_GRACE_HOURS = 1
  # # KICK LIMIT
  KICK_LIMIT = 10000
  # # remove failed requests flag
  DEL_FAILED = False

  # # request client
  __requestClient = None

  def requestClient( self ):
    """ request client getter """
    if not self.__requestClient:
      self.__requestClient = ReqClient()
    return self.__requestClient

  def initialize( self ):
    """ initialization """
    self.DEL_GRACE_DAYS = self.am_getOption( "DeleteGraceDays", self.DEL_GRACE_DAYS )
    self.log.info( "Delete grace period = %s days" % self.DEL_GRACE_DAYS )
    self.DEL_LIMIT = self.am_getOption( "DeleteLimit", self.DEL_LIMIT )
    self.log.info( "Delete limit = %s request/cycle" % self.DEL_LIMIT )
    self.DEL_FAILED = self.am_getOption( "DeleteFailed", self.DEL_FAILED )
    self.log.info( "Delete failed requests: %s" % { True: "yes", False: "no"}[self.DEL_FAILED] )

    self.KICK_GRACE_HOURS = self.am_getOption( "KickGraceHours", self.KICK_GRACE_HOURS )
    self.log.info( "Kick assigned requests period = %s hours" % self.KICK_GRACE_HOURS )
    self.KICK_LIMIT = self.am_getOption( "KickLimit", self.KICK_LIMIT )
    self.log.info( "Kick limit = %s request/cycle" % self.KICK_LIMIT )

    # # gMonitor stuff
    gMonitor.registerActivity( "DeletedRequests", "Deleted finished requests",
                               "CleanReqDBAgent", "Requests/min", gMonitor.OP_SUM )
    gMonitor.registerActivity( "KickedRequests", "Assigned requests kicked",
                               "CleanReqDBAgent", "Requests/min", gMonitor.OP_SUM )
    return S_OK()

  def execute( self ):
    """ execution in one cycle """

    now = datetime.datetime.utcnow()
    kickTime = now - datetime.timedelta( hours = self.KICK_GRACE_HOURS )
    rmTime = now - datetime.timedelta( days = self.DEL_GRACE_DAYS )

    # # kick
    statusList = [ "Assigned" ]
    requestIDsList = self.requestClient().getRequestIDsList( statusList, self.KICK_LIMIT )
    if not requestIDsList["OK"]:
      self.log.error( "execute: %s" % requestIDsList["Message"] )
      return requestIDsList

    requestIDsList = requestIDsList["Value"]
    kicked = 0
    for requestID, status, lastUpdate in requestIDsList:
      reqStatus = self.requestClient().getRequestStatus( requestID )
      if not reqStatus['OK']:
        self.log.error( ( "execute: unable to get request status", reqStatus['Message'] ) )
        continue
      status = reqStatus['Value']
      if lastUpdate < kickTime and status == 'Assigned':
        getRequest = self.requestClient().peekRequest( requestID )
        if not getRequest["OK"]:
          self.log.error( "execute: unable to read request '%s': %s" % ( requestID, getRequest["Message"] ) )
          continue
        getRequest = getRequest["Value"]
        if getRequest and getRequest.LastUpdate < kickTime:
          self.log.info( "execute: kick assigned request (%s/'%s') in status %s" % ( requestID,
                                                                                      getRequest.RequestName,
                                                                                      getRequest.Status ) )
          putRequest = self.requestClient().putRequest( getRequest )
          if not putRequest["OK"]:
            self.log.error( "execute: unable to put request (%s/'%s'): %s" % ( requestID,
                                                                               getRequest.RequestName,
                                                                               putRequest["Message"] ) )
            continue
          else:
            self.log.verbose( "Kicked request %d" % putRequest['Value'] )
          kicked += 1
      #   else:
      #     self.log.info('Not kicking request: %s' % requestID)
      #     if getRequest.LastUpdate > kickTime:
      #       self.log.info("Running notify: %s" % getRequest._Status)
      #       getRequest._notify()
      #       putRequest = self.requestClient().putRequest( getRequest )
      #       if not putRequest["OK"]:
      #         self.log.error( "execute: unable to put request (%s/'%s'): %s" % ( requestID,
      #                                                                            getRequest.RequestName,
      #                                                                            putRequest["Message"] ) )
      #       else:
      #         self.log.info("Updated Requestsshould")
      # else: # not old, or status not assigned
      #   self.log.info('Status is %s, should kick? %s' %(status, lastUpdate < kickTime, ))
      #   if status in ('Done', 'Failed'):
      #     self.log.info('Seems like request has fixed itself and should be put back: %s' % requestID)




    # # delete
    statusList = [ "Done", "Failed", "Canceled" ] if self.DEL_FAILED else [ "Done" ]
    requestIDsList = self.requestClient().getRequestIDsList( statusList, self.DEL_LIMIT )
    if not requestIDsList["OK"]:
      self.log.error( "execute: %s" % requestIDsList["Message"] )
      return requestIDsList

    requestIDsList = requestIDsList["Value"]
    deleted = 0
    for requestID, status, lastUpdate in requestIDsList:
      if lastUpdate < rmTime:
        self.log.info( "execute: deleting request '%s' with status %s" % ( requestID, status ) )
        delRequest = self.requestClient().deleteRequest( requestID )
        if not delRequest["OK"]:
          self.log.error( "execute: unable to delete request '%s': %s" % ( requestID, delRequest["Message"] ) )
          continue
        deleted += 1
        
    #self.kickScheduled()

    self.kickScheduled()

    gMonitor.addMark( "KickedRequests", kicked )
    gMonitor.addMark( "DeletedRequests", deleted )
    self.log.info( "execute: kicked assigned requests = %s" % kicked )
    self.log.info( "execute: deleted finished requests = %s" % deleted )
    return S_OK()

  def kickScheduled(self):
    """Kick requests that have been scheduled for more than 1 week."""
    now = datetime.datetime.utcnow()
    kickTime = now - datetime.timedelta(hours=7 * 24)
    statusList = ["Scheduled"]
    requestIDsList = self.requestClient().getRequestIDsList(statusList, self.KICK_LIMIT)
    if not requestIDsList["OK"]:
      self.log.error("execute: %s" % requestIDsList["Message"])
      return requestIDsList

    requestIDsList = requestIDsList["Value"]
    kicked = 0
    for requestID, status, lastUpdate in requestIDsList:
      reqStatus = self.requestClient().getRequestStatus(requestID)
      if not reqStatus['OK']:
        self.log.error("execute: unable to get request status", reqStatus['Message'])
        continue
      status = reqStatus['Value']

      if status != 'Scheduled':
        continue

      if lastUpdate > kickTime:
        self.log.info("Request %s has not been scheduled for more than 1 week" % requestID)
        continue

      getRequest = self.requestClient().peekRequest(requestID)
      if not getRequest["OK"]:
        self.log.error("execute: unable to read request '%s': %s" % (requestID, getRequest["Message"]))
        continue
      getRequest = getRequest["Value"]
      if getRequest and getRequest.LastUpdate < kickTime:
        self.makeRequestWaiting(getRequest)
        self.log.info("execute: kick scheduled request (%s/'%s') in status %s" % (requestID,
                                                                                  getRequest.RequestName,
                                                                                  getRequest.Status))
        putRequest = self.requestClient().putRequest(getRequest)
        if not putRequest["OK"]:
          self.log.error("execute: unable to put request (%s/'%s'): %s" % (requestID,
                                                                           getRequest.RequestName,
                                                                           putRequest["Message"]))
          continue
        else:
          self.log.verbose("Kicked request %d" % putRequest['Value'])
        kicked += 1
    self.log.info("Execute: kicked scheduled requests = %s" % kicked)
    return S_OK()

  def makeRequestWaiting(self, request):
    for operation in request:
      for lfn in operation:
        self.log.info("Setting %s to Waiting" % lfn.LFN)
        lfn.Status = 'Waiting'
    self.log.info("Request is Waiting?:\n%s" % request)
