from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
# link = 'http://suninjuly.github.io/redirect_page.html'

try:
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  #line for OS unix
    # browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)

    jump_button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
    jump_button.click()

    time.sleep(1)
    new_tab = browser.window_handles[1]
    browser.switch_to(new_tab)
    browser.switch_to.window(new_tab)

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
