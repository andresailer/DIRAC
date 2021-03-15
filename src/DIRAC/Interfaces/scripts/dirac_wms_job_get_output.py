#!/usr/bin/env python
########################################################################
# File :   dirac-wms-job-get-output
# Author : Stuart Paterson
########################################################################
"""
Retrieve output sandbox for a DIRAC job

Usage:
  dirac-wms-job-get-output [options] ... JobID ...

Arguments:
  JobID:    DIRAC Job ID or a name of the file with JobID per line

Example:
  $ dirac-wms-job-get-output 1
  Job output sandbox retrieved in 1/
"""
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

__RCSID__ = "$Id$"

import os
import shutil

import DIRAC
from DIRAC.Core.Utilities.DIRACScript import DIRACScript


@DIRACScript()
def main(self):  # pylint: disable=no-value-for-parameter
  self.registerSwitch("D:", "Dir=", "Store the output in this directory")
  self.registerSwitch("f:", "File=", "Get output for jobs with IDs from the file")
  self.registerSwitch("g:", "JobGroup=", "Get output for jobs in the given group")

  self.parseCommandLine(ignoreErrors=True)
  args = self.getPositionalArgs()

  from DIRAC.Interfaces.API.Dirac import Dirac, parseArguments
  from DIRAC.Core.Utilities.Time import toString, date, day
  from DIRAC.Core.Utilities.File import mkDir

  dirac = Dirac()
  exitCode = 0
  errorList = []

  outputDir = None
  group = None
  jobs = []
  for sw, value in self.getUnprocessedSwitches():
    if sw in ('D', 'Dir'):
      outputDir = value
    elif sw.lower() in ('f', 'file'):
      if os.path.exists(value):
        jFile = open(value)
        jobs += jFile.read().split()
        jFile.close()
    elif sw.lower() in ('g', 'jobgroup'):
      group = value
      jobDate = toString(date() - 30 * day)

      # Choose jobs in final state, no more than 30 days old
      result = dirac.selectJobs(jobGroup=value, date=jobDate, status='Done')
      if not result['OK']:
        if "No jobs selected" not in result['Message']:
          print("Error:", result['Message'])
          DIRAC.exit(-1)
      else:
        jobs += result['Value']
      result = dirac.selectJobs(jobGroup=value, date=jobDate, status='Failed')
      if not result['OK']:
        if "No jobs selected" not in result['Message']:
          print("Error:", result['Message'])
          DIRAC.exit(-1)
      else:
        jobs += result['Value']

  for arg in parseArguments(args):
    if os.path.isdir(arg):
      print("Output for job %s already retrieved, remove the output directory to redownload" % arg)
    else:
      jobs.append(arg)

  if not jobs:
    print("No jobs selected")
    DIRAC.exit(0)

  if group:
    if outputDir:
      outputDir = os.path.join(outputDir, group)
    else:
      outputDir = group

  if outputDir:
    mkDir(outputDir)
  else:
    outputDir = os.getcwd()

  jobs = [str(job) for job in jobs]
  doneJobs = os.listdir(outputDir)
  todoJobs = [job for job in jobs if job not in doneJobs]

  for job in todoJobs:

    result = dirac.getOutputSandbox(job, outputDir=outputDir)

    jobDir = str(job)
    if outputDir:
      jobDir = os.path.join(outputDir, job)
    if result['OK']:
      if os.path.exists(jobDir):
        print('Job output sandbox retrieved in %s/' % (jobDir))
    else:
      if os.path.exists('%s' % jobDir):
        shutil.rmtree(jobDir)
      errorList.append((job, result['Message']))
      exitCode = 2

  for error in errorList:
    print("ERROR %s: %s" % error)

  DIRAC.exit(exitCode)


if __name__ == "__main__":
  main()
