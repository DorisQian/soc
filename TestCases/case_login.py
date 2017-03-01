#! usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Doris"

import unittest
from Pages.Main import MainPage
from PublicMethod.operbrowser import OperationBrowser


class LoginTest:

    """用户名、密码为空"""
    def user_pwd_null(self):
        dr = OperationBrowser.openbrowser(self.driver)
        MainPage.username(self.driver).send_keys("")
        MainPage.password(self.driver).send_keys("")
        self.assertEqual(MainPage.hints(), "用户名、密码不可空")

if __name__ == "__main__":
    unittest.main()


