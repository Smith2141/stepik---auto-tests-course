from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
# link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver/chromedriver')  # line for OS unix
    # browser = webdriver.Chrome()  #line for WinOS
    browser.get(link)

    elem1 = int(browser.find_element(By.ID, "num1").text)
    elem2 = int(browser.find_element(By.ID, "num2").text)
    result = str(elem1 + elem2)
    assert result, "Нет результата сложения"

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(result)

    sb_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    sb_button.click()

finally:
    time.sleep(20)
    browser.quit()
