from selenium import webdriver
import time

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()

# Click on iframes link
driver.find_element_by_link_text("iFrame").click()

# To switch on iframe
# use frame id, frame name, frame index or Web element
driver.switch_to.frame("mce_0_ifr")

# clear the textbox inside frame
driver.find_element_by_css_selector("body[id= 'tinymce']").clear()

# Enter data in frame
driver.find_element_by_css_selector("body[id= 'tinymce']").send_keys("I am able to automate")

# To come out of original window or driver
driver.switch_to.default_content()

# find title or tag name of original page
print(driver.find_element_by_tag_name("h3"))

time.sleep(3)
driver.close()