from selenium import webdriver

# create object of webdriver
driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Enter data into textbox
driver.find_element_by_name('fld_username').send_keys('Chandrakant Kotage')
# driver.find_element_by_name('fld_email').send_keys('kchandu0143@gmail.com')
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys('kchandu0143@gmail.com')
driver.find_element_by_name('fld_password').send_keys('SwamiSamarth@1')
driver.find_element_by_name('fld_cpassword').send_keys('SwamiSamarth@1')

# if i enter the new input to the username field it will append to the existing one
# not override as Chandrakant Kotage Topper
driver.find_element_by_name('fld_username').send_keys(' Topper')

# if we want to enter new input then need to clear first
driver.find_element_by_name('fld_username').clear()
driver.find_element_by_name('fld_username').send_keys('Topper')

# driver.find_element_by_id('datepicker').send_keys('08/06.1992')
driver.find_element_by_name('phone').send_keys('7722071796')
driver.find_element_by_name('address').send_keys('Pune')
