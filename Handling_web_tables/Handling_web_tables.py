# https://cosmocode.io/automation-practice-webtable/

from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()

# get number of rows
rows = len(driver.find_elements_by_xpath("//table[@id = 'countries']/tbody/tr"))
print("Number of rows ", rows)

# get number of columns
columns = len(driver.find_elements_by_xpath("//tr[1]/td"))
print("Number of columns ", columns)

# get header data
columns_heading = driver.find_elements_by_xpath("//tr[1]/td")
for data in columns_heading:
    print(data.text, end = ' ')

# to select all checkbox
check_boxes = driver.find_elements_by_xpath("//input[@class = 'hasVisited']")
for i in check_boxes:
    i.click()
    print(i.is_selected())

# get all country column values
all_countries = driver.find_elements_by_xpath("//tr/td[2]")
for country in all_countries:
    print(country.text)




# for getting all row data
#all_rows_data = driver.find_elements_by_xpath("")
driver.close()