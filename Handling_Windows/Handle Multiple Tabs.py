from selenium import webdriver

driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.thetestingworld.com/testings/")

driver.find_element_by_xpath("//label[text()= 'Login']").click()
driver.find_element_by_xpath("//input[@name = '_txtUserName']").send_keys('Chandrakant Kotage')
driver.find_element_by_xpath("//input[@name='_txtPassword']").send_keys('Abcd@123')
driver.find_element_by_xpath("//input[@value = 'Login']").click()
driver.find_element_by_xpath("//a[contains (text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains (text(),'Delete')]").click()

Alltabs = driver.window_handles

for tabs in Alltabs:
    driver.switch_to.window(tabs)
    if driver.current_url == 'https://www.thetestingworld.com/testings/manage_customer.php':
        driver.find_element_by_xpath("//button[text() = 'Start Download']").click()

driver.switch_to.default_content()



driver.quit()