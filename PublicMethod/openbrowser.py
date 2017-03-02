#! usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

__author__ = "Doris"


class OperationBrowser:

    def __init__(self):
        self.profileDir = "C:\\Users\doris\AppData\Roaming\Mozilla\Firefox\Profiles\\4wdutv6c.default"
        self.profile = webdriver.FirefoxProfile(self.profileDir)
        self.driver = webdriver.Firefox(self.profile)

    def open_browser(self):
        self.driver.get('https://172.17.1.201/SOC2.0')
#        self.driver.maximize_window()
        time.sleep(3)

    def close_browser(self):
        self.driver.quit()
