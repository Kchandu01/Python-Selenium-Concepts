from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")

driver.maximize_window()

# work on radio button, click on radio button
driver.find_element_by_xpath("//input[@value='home']").click()
driver.find_element_by_xpath("//input[@value= 'office']").click()
