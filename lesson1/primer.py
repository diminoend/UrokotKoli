#импорт библиотек
from selenium import webdriver
import time




# создание переменной с вызовом вебдрайвера в котором указываем путь до драйвера браузера
wd = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
# открытие странички
wd.get('https://uchi.ru/')
# на весь экран
wd.maximize_window()
#создание переменной с селектором логина через id
login = wd.find_element_by_id('login')
#ввод логина
login.send_keys('wegweg@mail.ru')
#пауза на 3 секунды перед взаимодействием с полем ввода для пароля
time.sleep(1)
#создание переменной с селектором пароля через xpath
password = wd.find_element_by_xpath('/html/body/main/section/div[2]/div/form/div[2]/input')
#ввод пароля
password.send_keys('wegweg@mail.ru')
# сохдание переменной с селектором кнопки войти через xpath
log_in = wd.find_element_by_xpath('/html/body/main/section/div[2]/div/form/input[4]')
#клик по кнопке войти
log_in.click()
# Не пойму какая должна быть команда для ввода через CSS
plateclass = wd.find_element_by_css_selector('PlateClass').click()

#закрытие браузера
#wd.close()