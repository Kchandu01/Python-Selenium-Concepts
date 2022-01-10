import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# Implicit wait is global wait, it is valid for whole test
driver.implicitly_wait(10)
"""
Implicit wait:
    wait until 5 sec if object is not displayed,
    It is a global wait,
    if object is displayed in 2 sec then execution will resume in 2 sec
    if object do not show up at all, then max time your test waits for 5 seconds 
"""

# To validate correct page loaded or not Method 1
# By extracting title
title = driver.find_element_by_xpath("//div[@class = 'brand greenLogo']").text
assert title == 'GREENKART'

# Method 2 by extracting page title
assert driver.title == 'GreenKart - veg and fruits kart'

# searching ber in search bar and seeing the outcome product
driver.find_element_by_xpath("//input[@type='search']").send_keys('ber')
driver.find_element_by_css_selector("button.search-button").click()

# To validate the total displayed qty are as expected
total_count = len(driver.find_elements_by_xpath("//div[@class = 'product']"))
assert total_count == 3

time.sleep(3)
# To click on buttons
all_buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
print(len(all_buttons))

time.sleep(3)
for button in all_buttons:
    button.click()

# To click on cart
driver.find_element_by_xpath("//img[@alt = 'Cart']").click()

# To click on Proceed to checkout
driver.find_element_by_xpath("//button[text()= 'PROCEED TO CHECKOUT']").click()


# To Enter promocode
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')

# to click on apply button
driver.find_element_by_class_name('promoBtn').click()

# use wait
wait = WebDriverWait(driver, 20)
wait.until(ec.presence_of_element_located((By.XPATH, "//span[text() ='Code applied ..!']")))
code = driver.find_element_by_xpath("//span[text()= 'Code applied ..!']").text

assert code == 'Code applied ..!'

time.sleep(10)
driver.close()