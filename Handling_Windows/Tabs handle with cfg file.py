"""
1. Used Screenshot Method
2. Used Configuration file by removing hardcoded data
3. Created Utilities directory and one ReadProperties file for reading data from config.cfg file
4. Imported ReadProperties file for dynamic data
"""

from selenium import webdriver
from Screenshot import TakeScreenshot
from configparser import ConfigParser
from Utilities.ReadProperties import ReadConfig

########################## Without ReadProperties file ####################################
# create object of ConfigParser class
# config = ConfigParser()
# To read data from config file
# config.read("../Configurations/Configure.cfg")

# To get data from config file
# username = config.get("Section1", 'username')      ##### Without ReadProperties file #####
# password = config.get('Section1', 'password')      ##### Without ReadProperties file #####
############################################################################################

# After importing ReadProperties file
username = ReadConfig.get_username()
password = ReadConfig.get_password()
# print(username1)
# print(password1)
driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.thetestingworld.com/testings/")

driver.find_element_by_xpath("//label[text()= 'Login']").click()
driver.find_element_by_xpath("//input[@name = '_txtUserName']").send_keys(username)
driver.find_element_by_xpath("//input[@name='_txtPassword']").send_keys(password)
driver.find_element_by_xpath("//input[@value = 'Login']").click()
# time.sleep(2)
driver.find_element_by_xpath("//a[contains (text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains (text(),'Delete')]").click()
TakeScreenshot.take_page_screenshot(driver, 'LoginAfter')

Alltabs = driver.window_handles

for tabs in Alltabs:
    driver.switch_to.window(tabs)
    print(driver.current_url)

driver.quit()
