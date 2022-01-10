import time

from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element_by_link_text("Click Here").click()

# To get child window id
driver.switch_to.window(driver.window_handles[1])

"""
driver.window_handles get child window ids in the format of
[parentid, childid1, childid2, etc]
"""
print(driver.find_element_by_tag_name("h3").text)
driver.close()

# to get back to parent window
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)

time.sleep(3)
driver.close()
