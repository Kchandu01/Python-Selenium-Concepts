## Import the 'modules' that are required for execution
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# global url_under_test


# We make use of the parametrize decorator to supply input arguments
# to the test function

@pytest.mark.parametrize("input_browser", ['chrome']) # 2 test   # if ['chrome', 'firefox'] then 4 tests
@pytest.mark.parametrize("input_url", ['https://www.lambdatest.com', 'https://www.duckduckgo.com'])
def test_url_on_browsers(input_browser, input_url):
    global driver
    if input_browser == "chrome":
        driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    #if input_browser == "firefox":
     #   driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    time.sleep(5)
    driver.close()