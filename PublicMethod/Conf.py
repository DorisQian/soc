#!usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Doris"

import xlrd

url = "https://172.17.1.201/SOC2.0"
reportadd = "G:\study\python\projects\soc\\reports"
image = "G:\study\python\projects\soc\images"
userinfo = "G:\study\python\projects\soc\Data\\userinfo.xlsx"


class Conf:

    user_info = xlrd.open_workbook(userinfo)
    user = user_info.sheets()[0]
    username = user.col_values(0)
    password = user.col_values(1)
    print(username)
    print(password)

# a = Conf()



