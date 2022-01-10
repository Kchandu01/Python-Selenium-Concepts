"""
What if i want to select check box with option2?
    By using get_attribute('value')
"""

from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# find the generic locator which will extract all checkboxes into list and use loop to
# iterate them and then click on each
checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")

# Total no. of checkboxes present
print(len(checkboxes))

# iterate the checkboxes and click on each
for checkbox in checkboxes:
    # For getting values of all checkboxes
    # print(checkbox.get_attribute('value'))

    # To click on only option2 out of all checkboxes
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()

    # To validate each checkbox is selected or not use is_selected() method
    # if it is selected it will return True and if not False
    # assert checkbox.is_selected()

# driver.close()
"""
Radio buttons:
Same for radio buttons but the only difference is that you cant select all radio button at once.
So dont use loop. find one and select one.
"""

# To select Radio2 button
driver.find_element_by_xpath("//input[@value = 'radio2']").click()

# To get all Radiobuttons present
RadioButtons = driver.find_elements_by_xpath("//input[@type = 'radio']")

# To click on 3rd Radiobutton
# Index start with 0,1,2
RadioButtons[2].click()                           # it will override the first-one only one will be select
assert RadioButtons[2].is_selected()



