from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

act = ActionChains(driver)
# get element
element = driver.find_element_by_css_selector("input.search-keyword")
# click the item
act.click(on_element= element)
# send keys
act.send_keys("cucumber")
# perform operation
act.perform()

driver.close()


# By executing java script
# driver.execute_script("documnet.getElementByName("name")[0].value = 'abcde'")