import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    """Переходим по ссылке"""
    browser.get(link)

    """ищем цену и ждем"""
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    """жмем кнопку подтверждения"""
    browser.find_element_by_id('book').click() #кликаем кнопку без сохранения в переменную

    """Как обычно проходим робокапчу с формулой"""
    """Находим X и считаем"""
    x_element = browser.find_element_by_id('input_value').text
    result = calc(x_element)

    """Пишем результат в инпут"""
    browser.find_element_by_id('answer').send_keys(result)

    """клик на кнопку"""
    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    """Всегда закрываем окно браузера, чтоб не мешали =)"""
    time.sleep(5)
    browser.quit()
