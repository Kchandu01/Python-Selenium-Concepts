# Checking text present in or not in webtable

from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2021/08")
driver.implicitly_wait(5)

table_body = driver.find_element_by_tag_name('tbody').text
#print(table_body)

assert 'Selenium' in table_body
print('Selenium Present in the table')

driver.close()

