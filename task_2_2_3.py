import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file1.txt')  # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

browser.get(link)

browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys('Shegutov')
browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys('Alik')
browser.find_element(By.XPATH, "//input[@name='email']").send_keys('Alik@Shegutov.ru')
browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(15)
