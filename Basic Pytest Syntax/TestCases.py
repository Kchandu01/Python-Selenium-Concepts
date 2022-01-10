"""
1. for specific test case:  pytest -k (common name)
2. Group Testcases together:
3. Execute Specific group:
4. Execute all other than specific group:
"""
from selenium import webdriver
import pytest


@pytest.mark.Smoke
def test_registration_valid_data():
    driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://thetestingworld.com/testings/")
    driver.maximize_window()


@pytest.mark.Sanity
def test_registration_invalid_data():
    driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://thetestingworld.com/testings/")
    driver.maximize_window()


def test_invalid_data():
    driver = webdriver.Chrome(r"D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("http://thetestingworld.com/testings/")
    driver.maximize_window()
