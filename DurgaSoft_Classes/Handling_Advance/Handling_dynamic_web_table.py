# handling Dynamic web table

from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2021/08")
driver.implicitly_wait(5)

# To find all columns
all_columns = driver.find_elements_by_xpath("//table[@id = 'customers']//th")
print("There are total Columns : " + str(len(all_columns)))

# validate columns
assert len(all_columns) == 5

# To get data from all columns
for data in all_columns:
    print(data.text, end=' ')
    # To check whether Country column is present or not
    if data.text == 'Country':
        print("Country is Present")
        break

assert data.text == 'Country'


# To find all rows
all_rows = driver.find_elements_by_xpath("//table[@id = 'customers']//tr")
print("\nTotal rows are", len(all_rows))


driver.close()
