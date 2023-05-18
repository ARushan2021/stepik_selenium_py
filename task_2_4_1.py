import os
import time
from math import log, sin

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), "$100"))
browser.find_element(By.CSS_SELECTOR, '#book').click()
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
func = log(abs(12*sin(int(x))))
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(func)
browser.find_element(By.CSS_SELECTOR, "#solve").click()
time.sleep(10)


