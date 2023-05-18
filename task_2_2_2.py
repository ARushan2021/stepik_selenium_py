from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

browser.get(link)

# Поиск на страничке значения переменной "х"
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
func = log(abs(12*sin(int(x))))
# скролл странички на 100 пикселей вниз
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(func)
robot_check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
# скролл что б кнопка была видна
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
robot_check.click()
robot_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
# скролл что б кнопка была видна
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
robot_rule.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
# скролл что б кнопка была видна
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)







