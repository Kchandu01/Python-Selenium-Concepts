import time

from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    time.sleep(5)
    driver.close()


@pytest.mark.usefixtures('setUp')
class TestFacebookLogin:

    def test_logincheck(self, setUp):

        email = self.driver.find_element_by_id('email')
        email.send_keys('kchandu0143@gmail.com')
        password = self.driver.find_element_by_id("pass")
        password.send_keys("CKaveri@0143")
        self.driver.find_element_by_xpath("//button[starts-with(@id, 'u_0_d')]").click()