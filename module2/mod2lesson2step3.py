from selenium import webdriver
import time

try:
    # browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  # line for OS unix
    browser = webdriver.Chrome()  #line for WinOS
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script('document.title="Script executing";')
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(5)
    browser.quit()