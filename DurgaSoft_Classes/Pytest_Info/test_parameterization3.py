"""
pytest_generate_tests – Define custom parameterization
In this Selenium Python tutorial, we will now look into the aspect of custom parameterization in pytest.
pytest_generate_tests is a useful hook through which you can parametrize tests and implement a custom
parameterization scheme in pytest. Arbitrary parameterization using pytest_generate_tests is done during
the collection phase. pytest_generate_tests is a function and not a fixture. The input argument to the
pytest_generate_tests is a metafunc object.

metafunc objects help to inspect a test function and generate tests according to the test configuration
(or values) specified in the class or module where a test function is defined. metafunc argument to
pytest_generate_tests gives some useful information about the test function:

A look at the name of the function.
A look at fixture names that the function requests.
Flexibility to see the code of the function.
The implementation of metafunc class can be found here. Below is the example code which demonstrates
the usage of pytest_generate_tests function for parameterization in pytest.

"""
# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# @pytest.mark.parametrize("input_browser", ['chrome', 'firefox'])
# @pytest.mark.parametrize("input_url", ['https://www.lambdatest.com', 'https://www.duckduckgo.com'])


def pytest_generate_tests(metafunc):
    if "input_browser" in metafunc.fixturenames:
        metafunc.parametrize("input_browser", ["chrome"])  # ["chrome", "firefox"]
    if "input_url" in metafunc.fixturenames:
        metafunc.parametrize("input_url", ["https://www.lambdatest.com", "https://www.duckduckgo.com"])


def test_url_on_browsers(input_browser, input_url):
    global web_driver
    if input_browser == "chrome":
        web_driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    # if input_browser == "firefox":
     #   web_driver = webdriver.Firefox()
    web_driver.maximize_window()
    web_driver.get(input_url)
    print(web_driver.title)
    sleep(5)
    web_driver.close()