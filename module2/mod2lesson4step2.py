import time
from selenium import webdriver

browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  #line for OS unix
# browser = webdriver.Chrome()  #line for WinOS

browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

time.sleep(5)
browser.quit()