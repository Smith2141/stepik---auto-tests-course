import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    # browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  # line for OS unix
    browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    ch_box_robot = browser.find_element(By.ID, "robotCheckbox")
    ch_box_robot.click()
    rd_button_robot = browser.find_element(By.ID, "robotsRule")
    rd_button_robot.click()
    sb_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    sb_button.click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
