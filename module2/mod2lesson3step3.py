from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  #line for OS unix
    # browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)

    journey_button = browser.find_element(By.CSS_SELECTOR, '.container > .btn-primary')
    journey_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    button.click()

finally:
    # ожидание чтобы скопировать код ответа
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
