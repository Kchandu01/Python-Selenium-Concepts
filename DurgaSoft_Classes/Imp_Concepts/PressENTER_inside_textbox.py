import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.google.com/')

driver.find_element_by_name('q').send_keys('iphone Mobile')
driver.find_element_by_name('q').send_keys(Keys.ENTER)

time.sleep(5)
driver.close()