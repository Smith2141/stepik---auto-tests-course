import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  # line for OS unix
    # browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    # time.sleep(2)
    input_answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    ch_box_robot = browser.find_element(By.ID, "robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", ch_box_robot)
    ch_box_robot.click()
    # time.sleep(2)
    rd_button_robot = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", rd_button_robot)
    rd_button_robot.click()
    # time.sleep(2)
    # time.sleep(3)
    button.click()

finally:
    time.sleep(9)
    browser.quit()
