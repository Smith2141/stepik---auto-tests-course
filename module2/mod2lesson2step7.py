from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    # browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  #line for OS unix
    browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-group [name = "firstname"]')
    input1.send_keys("Agent")
    input2 = browser.find_element(By.CSS_SELECTOR, '.form-group [name = "lastname"]')
    input2.send_keys("Smith")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-group [name = "email"]')
    input3.send_keys("smith-tester@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'information.txt')
    upload_elem = browser.find_element(By.CSS_SELECTOR, '[type = "file"]')
    upload_elem.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
