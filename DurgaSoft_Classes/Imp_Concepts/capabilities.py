from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Chrome(ChromeOptions  = options, executable_path=r'C:\WebDrivers\geckodriver.exe')
my_dict = driver.capabilities
print("Mozilla Firefox browser version is: " + str(my_dict['browserVersion']))
driver.quit()