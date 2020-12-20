from selenium import webdriver

"""path of chromedriver is defined in secrets"""
from secrets import _chrome_path

chrome_path = _chrome_path
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.onlinekhabar.com")
driver.find_element_by_xpath('//*[@id="news-feed"]/section[1]/div[1]/a').click()
