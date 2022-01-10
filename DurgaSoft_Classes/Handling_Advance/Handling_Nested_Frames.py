"""
Nested Frames:
    In this Nested frames there are two frames
    1. frame-top
    (Inside the top frame 3 child frames
        a. LEFT
        b. MIDDLE
        C. RIGHT )
    2. frame-bottom

    So total 1(+3) + 1 = 5 Frames
"""

from selenium import webdriver
import time

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()

# Click on iframes link
driver.find_element_by_link_text("Nested Frames").click()

# Switch first to Parent Frame i.e. frame-top
top_frame_element = driver.find_element_by_xpath("//frame[@name = 'frame-top']")
driver.switch_to.frame(top_frame_element)

left_frame_element = driver.find_element_by_xpath("//frame[@name ='frame-left']")
# Now switch to first child frame i.e. LEFT Frame
driver.switch_to.frame(left_frame_element)

# Now get the text from LEFT Frame
print(driver.find_element_by_xpath("//body").text)

# Switch back to parent frame
driver.switch_to.parent_frame()

# Locate MIDDLE frame by web element
middle_frame_element = driver.find_element_by_xpath("//frame[@name = 'frame-middle']")

driver.switch_to.frame(middle_frame_element)

# Now get text
print(driver.find_element_by_xpath("//div[@id = 'content']").text)

# Now go the default content or web page
driver.switch_to.default_content()


bottom_frame_element = driver.find_element_by_xpath("//frame[@name = 'frame-bottom']")
driver.switch_to.frame(bottom_frame_element)

# Now get the text from BOTTOM Frame
print(driver.find_element_by_xpath("//body").text)

driver.close()

