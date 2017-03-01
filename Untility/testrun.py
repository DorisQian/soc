#! usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Doris"

import unittest
from TestCases.case_login import LoginTest

#suit = unittest.defaultTestLoader.discover("TestCases", pattern='case_*.py')
testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(LoginTest))

#if __name__ == '_main_':
runner = unittest.TextTestRunner()
print(3)
#runner.run()
runner.run(testunit)
