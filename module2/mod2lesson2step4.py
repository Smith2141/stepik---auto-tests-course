from selenium import webdriver
import time

try:
    # browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  # line for OS unix
    browser = webdriver.Chrome()  #line for WinOS
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    time.sleep(3)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # assert True


finally:
    time.sleep(5)
    browser.quit()