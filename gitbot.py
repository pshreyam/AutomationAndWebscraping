#!/usr/bin/python3

""" Test script for github login """

from selenium import webdriver
import time

from secrets import usr, pwd, _chrome_path 

class GithubBot:
    def __init__(self):
        chrome_path = _chrome_path
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.get("https://github.com")
    
    def login(self, username, password):
        self._username = username
        self._password = password
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(self._username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self._password)
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        print("Quit Driver")
        self.driver.quit()


g_bot = GithubBot()
g_bot.login(usr, pwd)
