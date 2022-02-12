from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.capabilities["browser_name"]
driver.get("http://www.google.com")

search_box = driver.find_element_by_name('q')
search_box.send_keys('Chandrakant')

search_box.send_keys(Keys.ENTER)

# search_button = driver.find_element_by_name('btnK')
# search_button.click()

bodyText = driver.find_element_by_tag_name('body').text
print(bodyText)

assert 'Chandrakant' in bodyText

driver.close()