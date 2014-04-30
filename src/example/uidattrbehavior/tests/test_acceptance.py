# -*- coding: utf-8 -*- #
import unittest
import robotsuite

from plone.testing import layered
from example.uidattrbehavior.testing import (
    UIDATTRBEHAVIOR_ROBOT_TESTING
)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('acceptance'),
                layer=UIDATTRBEHAVIOR_ROBOT_TESTING),
    ])
    return suite
