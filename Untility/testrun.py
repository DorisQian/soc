#! usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

__author__ = "Doris"

suit = unittest.defaultTestLoader.discover("TestCases", pattern='case_*.py')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suit)


