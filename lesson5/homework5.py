'''
Задание:
Открыть Учиру и авторизоваться
Открыть новую вкладку с главной страничкой учи ру
Сделать скролл вниз
Сделать скролл вверх
Перейти в личный кабинет ученика или учителя
Переключиться на первую вкладку и закрыть её
Закрыть браузер
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PageObject.methods import *
import time

site = 'https://ts01.shot-uchi.ru/'
loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'

wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
wd.maximize_window()
# Открываем 1 вкладку
wd.get(site)
# Открываем новую вкладку с главной страничкой учи ру
wd.execute_script("window.open('https://ts01.shot-uchi.ru/');")
# Переход на 1 вкладку
wd.switch_to.window(wd.window_handles[0])
# Создание функции с авторизацией
def login():
    wd.find_element(*locator.login_input).send_keys(loginx)
    wd.find_element(*locator.password_input).send_keys(passwordx)
    wd.find_element(*locator.log_in_button).click()
# Переход на 2 вкладку
wd.switch_to.window(wd.window_handles[1])
# Скролл вниз
wd.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
time.sleep(1)
# Скролл вверх
wd.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_UP)
# Вызов функции авторизации
login()
# Переключение на 1 вкладку
wd.switch_to.window(wd.window_handles[0])
# Закрытие 1 вкладки
wd.close()
# Закрытие браузера
wd.quit()


