from selenium import webdriver
from Screenshot import TakeScreenshot

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://thetestingworld.com/testings/")
driver.maximize_window()

# Take screenshot as file
#driver.get_screenshot_as_file(r"C:\Users\chandrakant-kotage\PycharmProjects\PyTest_All_Concepts\Screenshots\Before_Reg.png")

# by calling method
TakeScreenshot.take_page_screenshot(driver, 'After')
driver.close()