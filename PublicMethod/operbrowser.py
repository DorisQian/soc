#! usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Doris"

from selenium import webdriver


class OperationBrowser:

    def open_browser(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://172.17.1.201/SOC2.0')
        self.driver.maximize_windows()
        self.driver.implicitly_wait(10)
        return driver

    def close_browser(self):
        self.driver.quit()


