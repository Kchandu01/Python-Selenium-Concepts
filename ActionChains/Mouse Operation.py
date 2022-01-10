from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/")
# driver.find_element_by_link_text("Login").click()

act = ActionChains(driver)

# Click Operation
# act.click().perform()  # wherever is the control just click i.e. left click
# act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()   # left click by locating element

# context click or Right click
#act.context_click().perform()  # right click wherever the control
#act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Double click opearation
#act.double_click().perform()  # double click anywhere
#act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()  # double click by locating element

# Moving a Mouse to Menu and Menu will open
act.move_to_element(driver.find_element_by_xpath("//span[text()='TUTORIAL ']")).perform()


time.sleep(10)
driver.close()