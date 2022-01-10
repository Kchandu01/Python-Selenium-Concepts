import time

from selenium import webdriver


driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://rahulshettyacademy.com/angularpractice/")
# to refresh the browser
driver.refresh()

# inputting values in the text box with help of Javascript executor
driver.execute_script("document.getElementsByName('name')[0].value='abcde'")
driver.execute_script("window.scrollTo(0,400);")
driver.execute_script("document.getElementsByName('email')[0].value = 'kchandu'")

time.sleep(10)
driver.quit()

"""
Document.getElementById()
Returns an object reference to the identified element.

Document.getElementsByName()
Returns a list of elements with the given name.

Document.getElementsByClassName()
Returns a list of elements with the given class name.

Document.getElementsByTagName()
Returns a list of elements with the given tag name.

Document.getElementsByTagNameNS()
Returns a list of elements with the given tag name and namespace.
"""
