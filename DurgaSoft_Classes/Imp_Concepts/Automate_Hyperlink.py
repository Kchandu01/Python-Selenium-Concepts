from selenium import webdriver

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qafeast.com/demo")
#driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/ul/li[6]").click()
driver.find_element_by_xpath("//html[@id='block-one']/div/div/div[1]/div/ul/li[6]]")
driver.find_element_by_link_text("Web browser automation").click()