"""
Functional Automation of e-commerce app:

Test Case- 1: Validate whether products selected in page-1 are showing in page-2 check page.

Test Case- 2: Verify if prices decreases on discount

Test Case-3: Verify if sum of products in check-out page matches with total amount
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Next, the instance of Chrome WebDriver is created.
driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# driver.implicitly_wait(10)

# Find search box
driver.find_element_by_css_selector("input.search-keyword").send_keys('ber')

# Alternative method to send data

# To enter search button
driver.find_element_by_css_selector("button.search-button").click()

# time.sleep(2)
# To validate the total displayed qty are as expected
Qty_count = len(driver.find_elements_by_xpath("//div[@class = 'product']"))
assert Qty_count == 3

time.sleep(3)
# To click on add to cart button
buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")

# To get all product names
Products_list = []
# To click on all buttons
for button in buttons:
    # Method-2
    # Complete xpath : //div[@class = 'product-action']/button/parent::div/parent::div/h4
    # But, already my control is at button so write only
    Products_list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(Products_list)
"""
When we say driver.find_element then the search will start from Top-left side from the begining.
when we say button.find_element then search will start from that point.
If we want traverse back to your parent from child (bottom to up) then we must use Xpath
CSS do not have any provision to traverse back.
"""

""" 
Method -1 :
# To get product name one method is find one generic locator and use loop i.e.
names = driver.find_elements_by_xpath("//h4[@class = 'product-name']")

# to get all products names
for name in names:
    print(name.text)
    
"""

# To click on Cart
driver.find_element_by_xpath("//img[@alt = 'Cart']").click()

# to click on Proced To CheckOut
driver.find_element_by_xpath("//button[text() = 'PROCEED TO CHECKOUT']").click()

# To confirm added items are present in final list or not
Final_list = []
time.sleep(2)
items = driver.find_elements_by_css_selector("p.product-name")
for item in items:
    Final_list.append(item.text)

print(Final_list)

# To validate the added and final items list are confirmedd
assert Products_list == Final_list

# Get amount before applying code
Original_amount = driver.find_element_by_css_selector('span.discountAmt').text

# To Enter promocode in textbox
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'promoCode'))).send_keys('rahulshettyacademy')

# to click on PromoApply button
driver.find_element_by_xpath("//button[@class = 'promoBtn']").click()

# To check whether promo code applied or not
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'promoInfo')))
PromoInfo = driver.find_element_by_class_name("promoInfo").text

# After Promocode applied
Discount_Amount = driver.find_element_by_css_selector('span.discountAmt').text

# The discounted amount should always be less than original amount
assert float(Discount_Amount) < int(Original_amount)

# To validate Info
assert PromoInfo == 'Code applied ..!'

# Test Case 3: Verify if sum of products in check-out page matches with total amount
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

# get total amount to comapre
Total_Amt = driver.find_element_by_css_selector("span.totAmt").text

assert sum == int(Total_Amt)



time.sleep(5)
driver.close()

"""
Assignment:
verify is search functionality in home page is working or not
search 'ber'
3 products = x,y,z

FOr cheat sheet:
email: mentor@rahulshettyacademy.com
"""
