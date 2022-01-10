import time
from selenium import webdriver

driver = webdriver.Chrome("D:\My Folder\DS\Python Automation\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get(" https://www.qafeast.com/demo")

"""
How to automate text box in Selenium webdriver?
There are different operations we can perform in the text box using the 
selenium web driver.

The operations are:

1. Type in the text box: To type , send_keys() method used to pass the Keyboard 
   keys or text into editable elements (text bar, text area) without replacing the 
   previously available content.
2. Editable or not:  is_enabled()  method used to verify if the web element 
   is enabled or disabled within the webpage. 
3. Get the text:  text method is used to get the text of the element.
4. Clear: We can clear any editable field using a clear() method present in 
   selenium, most of the time clear() will be used when the text typed.

"""
# 1. Enter text in textbox:
driver.find_element_by_xpath("//input[@id = 'editabletext']").send_keys('Selenium')

# 2. Check editable or not
text_box = driver.find_element_by_id('noteditabletext')
if text_box.is_enabled():
    print("Text box is editable")
else:
    print('text box is non editable')

# 3. Get the text: To get the text from the text box
text_box1 = driver.find_element_by_xpath("//input[@value = 'Enter username']").get_attribute('value')
print(text_box1)

# 4. To clear the text
driver.find_element_by_xpath("//div[@class='form-group'][3]/input[@id='editabletext']").clear()

time.sleep(5)
driver.close()