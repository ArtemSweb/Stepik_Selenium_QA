import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    """Перейти по ссылке на первый экран"""
    browser.get(link)
    time.sleep(1)

    """Кликнуть по ссылке для перехода на второй экран задания"""
    first_btn = browser.find_element_by_css_selector('[type="submit"]')
    first_btn.click()

    """Перехватываем и принимаем alert"""
    alert = browser.switch_to.alert
    alert.accept()

    """Находим X и считаем"""
    x_element = browser.find_element_by_id('input_value').text
    result = calc(x_element)

    """Пишем результат в инпут"""
    input_zone = browser.find_element_by_id('answer')
    input_zone.send_keys(result)

    """клик на кнопку"""
    last_btn = browser.find_element_by_css_selector('[type="submit"]')
    last_btn.click()

finally:
    """Всегда закрываем окно браузера, чтоб не мешали =)"""
    time.sleep(5)
    browser.quit()
