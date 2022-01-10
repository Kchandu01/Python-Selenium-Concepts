import time
from selenium import webdriver
from Screenshot import TakeScreenshot

# create object for webdriver
#def test_registration_verify():
driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('http://www.thetestingworld.com/testings/')

driver.find_element_by_xpath("//label[text() = 'Login']").click()
driver.find_element_by_xpath("//input[@name= '_txtUserName']").send_keys('chandrakant kotage')
driver.find_element_by_xpath("//input[@name= '_txtPassword']").send_keys('Abcd@123')
driver.find_element_by_xpath("//input[@type = 'submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(), 'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()

Allwindows = driver.window_handles
print(Allwindows)
for win in Allwindows:
    driver.switch_to.window(win)
    print(driver.current_url)
    if driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php":
        print('Hello')
        driver.find_element_by_xpath("//button[text()='Start Download']").click()
        time.sleep(5)
        TakeScreenshot.take_page_screenshot(driver, 'downloadbutton1')
        time.sleep(20)
    else:
        print('I m not entered inside')


