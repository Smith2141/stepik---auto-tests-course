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
    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x)
    # input_answer = browser.find_element(By.ID, "answer")
    # input_answer.send_keys(y)
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None
    # ch_box_robot = browser.find_element(By.ID, "robotCheckbox")
    # ch_box_robot.click()
    # rd_button_robot = browser.find_element(By.ID, "robotsRule")
    # rd_button_robot.click()
    # sb_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # sb_button.click()

finally:
    time.sleep(3)
    browser.close()
    browser.quit()