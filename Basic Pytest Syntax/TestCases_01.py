import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def environmental_setup():
    # create object of webdriver
    global driver
    driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()


a = 10


@pytest.mark.skipif(a > 100, reason='a is out of range so we dont need this test here')
def test_homepage(environmental_setup):
    # working on textbox
    driver.find_element_by_xpath("//input[@name = 'fld_username']").send_keys('Chandrakant Kotage')
    driver.find_element_by_name("fld_email").send_keys('kchandu0143@gmail.com')

    # working on radio button
    driver.find_element_by_xpath("//input[@value = 'home']").click()

    # working on checkbox
    driver.find_element_by_name('terms').click()

    # Working on links
    driver.find_element_by_link_text('Read Detail').click()
    driver.find_element_by_link_text('X').click()


# @pytest.mark.skip("dont need thid test here")
def test_SelectCity(environmental_setup):
    # Working on Dropdown
    # while working on dropdown we need to import Select class and create object of that class
    #
    obj = Select(driver.find_element_by_id('countryId'))
    obj.select_by_visible_text('India')

    # Working on explicit wait
    # create object of webdriver wait
    wait = WebDriverWait(driver, 100)
    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), 'Delhi'))
    obj = Select(driver.find_element_by_id('stateId'))
    obj.select_by_visible_text('Delhi')

    wait.until(ec.text_to_be_present_in_element((By.ID, 'cityId'), 'Delhi'))
    obj = Select(driver.find_element_by_id('cityId'))
    obj.select_by_visible_text('Delhi')
