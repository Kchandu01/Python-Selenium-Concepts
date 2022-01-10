import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)

# Textbox
driver.find_element_by_xpath("//input[@name = 'name']").send_keys("Chandrakant Kotage")
driver.find_element_by_xpath("//input[@name ='email']").send_keys("kchandu0143@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Abcd@123")

# Checkbox
driver.find_element_by_id("exampleCheck1").click()

# Drop down
"""
# Drop-downs- (static and dynamic)
1. Static Means options are fixed not auto suggestive
(examples- Sex either male or female are fixed)
Static Drop-downs are handled by Select class.

2. Dynamic means options displayed upon what you entered they not fixed they are auto suggestive
(for examples- make my trip start destination)
"""
obj = Select(driver.find_element_by_id("exampleFormControlSelect1"))
obj.select_by_visible_text("Female")
obj.select_by_index(0)
# obj.select_by_value()

# Radio Button
driver.find_element_by_id("inlineRadio2").click()

# Birthdate
driver.find_element_by_name("bday").send_keys("08-06-1992")

# Button
driver.find_element_by_xpath("//input[@value = 'Submit']").click()

# to confirm success alert
# obj = driver.find_element_by_class_name("alert-success").get_attribute('value')   # to get value from textbox
alert_message = driver.find_element_by_class_name("alert-success").text  # to get alert message

# Assertion or validation
assert alert_message == "×\nSuccess! The Form has been submitted successfully!."

# or
assert "Success" in alert_message
"""
str1 = 'Hi my name is Apple'
# how to check substring in string
print("Apple" in str1)
# Outputs : True
"""


time.sleep(5)
driver.close()


"""
Absolute X-path:
    Generates X-path from the root of the html to the desired element.
    
Relative X-path:
    will directly target the desired element with attribute defined for it.
    
Relative x-path is better and used generally. But, why?
    bcz when change in page structure then absolute x-path will not work.
"""