import os
import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

browser.get(link)

browser.find_element(By.XPATH, '//button[@type="submit"]').click()
confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
func = log(abs(12*sin(int(x))))
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(func)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)



