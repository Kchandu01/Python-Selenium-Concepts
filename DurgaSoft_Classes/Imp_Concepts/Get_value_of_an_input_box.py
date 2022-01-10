from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qafeast.com/demo")


# The get_attribute() method is capable of obtaining the value we have entered in an input box.
# To get the value, we have to pass value as a parameter to the method.
text = driver.find_element_by_xpath("//input[@value='Enter username']").get_attribute('value')
print(text)
