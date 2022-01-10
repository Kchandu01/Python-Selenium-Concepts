import time

from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

validate_text = 'Option3'
driver.find_element_by_id("name").send_keys(validate_text)
driver.find_element_by_id("alertbtn").click()

"""
To navigate through alert You cannot go direct with driver. you need to switch to that alert and by using that 
alert object you will handle the alert.
"""
# Create object of alert
alert = driver.switch_to.alert

# To validate the given text is present in alert or not
Alerttext = alert.text

assert validate_text in Alerttext
# print(alert.text)
alert.accept()

time.sleep(5)

# To scrolldown
driver.execute_script("window.scrollTo(0,300);")

# confirm alert button
driver.find_element_by_id("confirmbtn").click()

# creating object of alert
alert = driver.switch_to.alert

# To confirm the alert
# alert.accept()

# To dismiss the alert or cancel
alert.dismiss()
"""
Two Types of Alerts:
    1. Message alert
    2. Confirm alert
    
    For alerts in positive scenario use alert.accept() and in negative scenario use alert.dismiss()
"""

