
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

msg_text = driver.find_element_by_xpath("//*[@id='content']/div[2]/span").text
print(msg_text)