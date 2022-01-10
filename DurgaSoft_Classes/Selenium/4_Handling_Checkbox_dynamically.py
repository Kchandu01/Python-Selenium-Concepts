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
    checkbox.click()

    # To validate each checkbox is selected or not use is_selected() method
    # if it is selected it will return True and if not False
    assert checkbox.is_selected()

driver.close()