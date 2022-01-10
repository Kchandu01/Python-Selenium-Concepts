from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@name = 'name']").send_keys("Chandrakant Kotage")
driver.find_element_by_xpath("//input[@name ='email']").send_keys("kchandu0143@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Abcd@123")
driver.find_element_by_id("exampleCheck1").click()

obj = Select(driver.find_element_by_id("exampleFormControlSelect1"))
obj.select_by_visible_text("Female")

driver.find_element_by_id("inlineRadio2").click()
driver.find_element_by_name("bday").send_keys("08-06-1992")
driver.find_element_by_xpath("//input[@value = 'Submit']").click()

# to confirm success alert
#obj = driver.find_element_by_class_name("alert-success").get_attribute('value')   # to get value from textbox
obj = driver.find_element_by_class_name("alert-success").text                      # to get alert message
print(obj)

str1 = 'Hi my name is chandrakant'
# (how to check substring in string)
print("chandrakant" in str1)
# Outputs : True