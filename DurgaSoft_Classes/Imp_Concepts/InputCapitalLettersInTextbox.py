from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get(" https://www.qafeast.com/demo")

# create object of actionschains
obj = ActionChains(driver)
textbox_source = driver.find_element_by_xpath("//input[@id='editabletext']")

# move cursor to that locator
obj.move_to_element(textbox_source)

# click
obj.click()

# perform clicking on shift button
obj.key_down(Keys.SHIFT)

# input letters in edit box
obj.send_keys("Selenium webdriver")

# perform action
obj.perform()