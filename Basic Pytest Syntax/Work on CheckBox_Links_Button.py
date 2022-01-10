import time
from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")

driver.maximize_window()

# work on check box
driver.find_element_by_xpath("//input[@name='terms']").click()

# work on button
driver.find_element_by_xpath("//input[@value='Sign up']").click()

# work on links
driver.find_element_by_link_text('Read Detail').click()
time.sleep(5)
driver.find_element_by_link_text('X').click()

driver.close()