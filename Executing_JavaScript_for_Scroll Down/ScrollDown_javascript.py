"""
    The scroll bar is not a part of the page, its part of the browser.
If its not a part of the page then it will not have any HTML Code.
So, we cannot Automate it using selenium.
So, whatever the task you want to do on browser you do it by javascript.

"""
from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://thetestingworld.com/testings/")
driver.maximize_window()

driver.execute_script('window.scrollTo(0,400);')
# first argument is to horizontal scroll and second one is verticle scroll in pixel format