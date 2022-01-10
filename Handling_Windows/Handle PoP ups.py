import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.dummysoftware.com/popupdummy_testpage.html")
MainWindow = ''  # for taking control after popups closed

# get all active windows unique key

Allwindow = driver.window_handles

# window handles gives uniq keys in list format
# print(Allwindow)

# for getting current url of all pop up windows run for loop for Allwindow
for win in Allwindow:
    driver.switch_to.window(win)
    print(driver.current_url)
    if driver.current_url == "http://www.dummysoftware.com/popupdummy_testpage.html":
        print('This is my Main Window')
        MainWindow = win         # # for taking control after popups closed
    else:
        driver.close()

# print(driver.current_url)
# if i try to get current url it will through this error
# selenium.common.exceptions.NoSuchWindowException: Message: no such window: target window already closed
# bcz the last window is close and the control was on last window
# so after closing these pop ups i want to take my control over my manin window

driver.switch_to.window(MainWindow)
print('My current window URL is: ', driver.current_url)