""" AlwaysProbingPolicy module """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from DIRAC import S_OK
from DIRAC.ResourceStatusSystem.PolicySystem.PolicyBase import PolicyBase

__RCSID__ = "$Id$"


class AlwaysProbingPolicy(PolicyBase):
    """
    The AlwaysProbingPolicy is a dummy module that can be used as example, it
    always returns Probing status.
    """

    @staticmethod
    def _evaluate(commandResult):
        """
        It returns Probing status, evaluates the default command, but its output
        is completely ignored.
        """

        policyResult = {"Status": "Probing", "Reason": "AlwaysProbing"}

        return S_OK(policyResult)
