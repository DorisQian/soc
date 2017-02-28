#!usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Doris"

class MainPage:

    @staticmethod
    def username(driver):
        element = driver.find_element_by_id("txtUserName")
        return element

    @staticmethod
    def password(driver):
        element = driver.find_element_by_id("txtPassword")
        return element

    @staticmethod
    def login(driver):
        element = driver.find_element_by_xpath("html/body/section/div/div[3]/div[6]/button")
        return element
