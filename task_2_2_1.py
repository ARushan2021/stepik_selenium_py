from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:

    browser.get(link)

    # Поиск на страничке значения переменной "х" и "y"
    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text

    # Вычисляем значение переменной x_response
    x_response = int(x) + int(y)
    print(f'x = {x}, y = {y}, ответ = {x_response}')

    # Заполняем поля на страничке
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(x_response))



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
