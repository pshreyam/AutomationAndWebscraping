from selenium import webdriver

"""Defined module"""
from secrets import _chrome_path

"""_chrome_path is mentioned in secrets module"""

chrome_path=_chrome_path
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.onlinekhabar.com/")

