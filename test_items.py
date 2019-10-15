from selenium.common.exceptions import NoSuchElementException

item_link = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def check_button_exist(browser):
    browser.get(item_link)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True


def test_add_cart_button_available_visitor(browser):
    assert check_button_exist(browser), 'Кнопка "Добавить в корзину" не найдена. Проверьте селектор элемента!'

#TODO: примеры запуска:
# pytest -sv --language=it ./test_items.py
# pytest -sv --browser_name=firefox --language=ar ./test_items.py
