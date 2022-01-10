from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")

driver.maximize_window()

# work on dropdown
# In Dropdown we select only one value and in list we can select more than one value

# Whenever you work on dropdown import Select class
# whenever you work on dropdown we need to create object of select class

obj = Select(driver.find_element_by_name('sex'))
# obj.select_by_index(1)   # index always start from zero, and index is integer
# obj.select_by_value("2")   # value is string
obj.select_by_visible_text("Male")



# Working on selecting country

obj = Select(driver.find_element_by_name("country"))
obj.select_by_visible_text('India')


# while working on list we can use ## we use deselect while working on list only
obj.deselect_by_visible_text()
obj.select_by_value()
obj.deselect_by_index()  # so it will remove all the selected items
