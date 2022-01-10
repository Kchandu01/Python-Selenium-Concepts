import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//li[@data-cy = 'account']").click()
driver.find_element_by_class_name("langCardClose").click()
# first need to click bcz after clicking only text box is opening
driver.find_element_by_id('fromCity').click()

driver.find_element_by_css_selector("input[placeholder = 'From']").send_keys("del")  # del typing randomly and here i want to search for delhi
time.sleep(3)
cities = driver.find_elements_by_xpath("//p[contains(@class, 'blackText')]")

# print(cities)
# cities = driver.find_elements_by_css_selector("p[class* = 'blackText']")
# Get the count of options using Len method and Sleep method to pause
print(len(cities))

# to print all city
for city in cities:
    print(city.text)
    if city.text == "Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text() = 'Delhi, India']").click()

# here city is webelement
# city only return webelement and text will extract the text from that webelement
"""
driver.find_elements_ : return type is list
"""
