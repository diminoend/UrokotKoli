# импорт библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service=s)
# открытие странички
wd.get('https://uchi.ru/')
# создание переменной с селектором логина через id
login = wd.find_element(By.ID, 'login')
# ввод логина
login.send_keys('1')
# пауза на 3 секунды перед взаимодействием с полем ввода для пароля
time.sleep(3)
# создание переменной с селектором пароля через xpath
password = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/div[2]/input')
# ввод пароля
password.send_keys('1')
# сохдание переменной с селектором кнопки войти через xpath
log_in = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]')
# клик по кнопке войти
log_in.click()
# закрытие браузера
wd.close()
