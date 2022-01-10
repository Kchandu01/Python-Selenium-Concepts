import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

@pytest.fixture
def start_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)

    yield
    time.sleep(10)
    driver.close()

# locate elements and send data
def test_RegistrationPage(start_browser):
    driver.find_element_by_xpath("//input[@name = 'name']").send_keys("Chandrakant Kotage")
    driver.find_element_by_xpath("//input[@name ='email']").send_keys("kchandu0143@gmail.com")
    driver.find_element_by_id("exampleInputPassword1").send_keys("Abcd@123")
    driver.find_element_by_id("exampleCheck1").click()

    obj = Select(driver.find_element_by_id("exampleFormControlSelect1"))
    obj.select_by_visible_text("Female")

    driver.find_element_by_id("inlineRadio2").click()
    driver.find_element_by_name("bday").send_keys("08-06-1992")
    driver.find_element_by_xpath("//input[@value = 'Submit']").click()

    # to confirm success alert
    obj = driver.find_element_by_class_name("alert-success").text

    assert obj == "×\nSuccess! The Form has been submitted successfully!."





