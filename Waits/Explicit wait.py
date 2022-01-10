from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ew
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture()
def environmental_setup():
    global driver
    driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://www.thetestingworld.com/testings/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()


def test_registration_Page(environmental_setup):
    wait = WebDriverWait(driver, 100)
    wait.until(ew.text_to_be_present_in_element((By.ID, 'countryId'), 'India'))
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("India")

    wait.until(ew.text_to_be_present_in_element((By.ID, 'stateId'), 'Delhi'))
    obj = Select(driver.find_element_by_id('stateId'))
    obj.select_by_visible_text('Delhi')

    wait.until(ew.text_to_be_present_in_element((By.ID, 'cityId'), ''))
