from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  #line for OS unix
    # browser = webdriver.Chrome()  #line for WinOS

    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    # говорим Selenium проверять в течение 20 секунд, пока цена не станет равна $100
    price = WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), text_='$100')
        )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    browser.implicitly_wait(5)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    sb_button = browser.find_element(By.ID, "solve")
    sb_button.click()

finally:
    time.sleep(15)
    browser.quit()
