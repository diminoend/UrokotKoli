#импорт библиотек
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



# создание переменной с вызовом вебдрайвера в котором указываем путь до драйвера браузера
wd = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
# на весь экран
wd.maximize_window()
# открытие странички
wd.get('https://uchi.ru/')
# создание переменной с селектором логина через id
login = wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
# ввод логина
# login.send_keys('wegweg@mail.ru')
# пауза на 3 секунды перед взаимодействием с полем ввода для пароля
time.sleep(1)
# создание переменной с селектором пароля через xpath
password = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/div[2]/input').send_keys('wegweg@mail.ru')
# ввод пароля
# password.send_keys('wegweg@mail.ru')
# сохдание переменной с селектором кнопки войти через xpath
log_in = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
# клик по кнопке войти
# log_in.click()
# Создание переменной для списка классов через CSS. Не пойму какая должна быть команда
# plateclass = wd.find_element(By.NAME, 'PlateClass').click()
# нажатие на чат
wd.find_element(By.ID, 'chat-icon').click()
# закрытие браузера
wd.close()