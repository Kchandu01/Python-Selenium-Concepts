from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")

driver.find_element_by_name('fld_username').send_keys('Hello')

act = ActionChains(driver)
# act.send_keys(Keys.TAB).perform()

# CONTROL + a is used to select data from text box
act.key_down(Keys.CONTROL).send_keys('a').perform()

# for CONTROL + ALT + DELETE

act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
time.sleep(10)

