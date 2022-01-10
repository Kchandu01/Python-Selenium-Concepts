from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dummysoftware.com/popupdummy_testpage.html")
# driver.get("http://www.thetestingworld.com/testings")
driver.implicitly_wait(10)

all_windows = driver.window_handles
main_win = ''

try:
    for win in all_windows:
        driver.switch_to.window(win)
        print(driver.current_url)

        # if driver.current_url == "http://www.thetestingworld.com/testings":
        if driver.current_url == "http://www.dummysoftware.com/popupdummy_testpage.html":
            main_win = win

        else:
            driver.close()

except Exception as e:
    print(e)
    print("Page has no pop-ups")
    print("except block has executed")

finally:
    print("finally block has executed")
    driver.switch_to.window(main_win)
    driver.close()
