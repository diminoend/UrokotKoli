# импорт библиотек
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\chromedriver\chromedriver.exe")

""" Флоу
- авторизация учителя
- переход в первый классбук из селектора в шапке
- Удаление ученика номер 1
- добавление нового ученика в класс
- Переход в ЛК
- Закрытие браузера
"""
# Автоматизация через локаторы xpath только по тегам
# создание переменной с вызовом вебдрайвера в котором указываем путь до драйвера браузера
wd = webdriver.Chrome(service=s)
# на весь экран
wd.maximize_window()
# открытие странички
wd.get('https://uchi.ru/')
# логин через id
wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
# пауза на 1 секунду перед взаимодействием с полем ввода для пароля
time.sleep(1)
# ввод пароля через xpath
wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/div[2]/input').send_keys('wegweg@mail.ru')
# кнопка войти через xpath
wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
# Не пойму какая должна быть команда для поиска через уникальный атрибут //div[@class='*PlateClass*'] . Поэтому xpath
wd.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div').click()
# Выбор первого класса в списке
wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/a[1]/a').click()
# Ждём онбординг 3 секунды, жмём Далее
time.sleep(3)
wd.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/div[3]/div[2]').click()
# Ищем и удаляем ученика номер 1
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div[10]/div').click()
# нажимаем принять во всплывашке
wd.switch_to.alert.accept()
# Жмём кнопку Добавить ученика
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button').click()
# ждём 1 секунду появления поля
time.sleep(1)
# Ищем 4 поле Фамилия и вводим - Глав.
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[5]/div/div[2]/input').send_keys('Глав')
# вводим Имя - Рыба
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[5]/div/div[3]/input').send_keys('Рыба')
# Выбираем Пол - М
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[5]/div/div[4]/label[1]').click()
# Жмём кнопку Сохранить
wd.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[5]/div/div[10]/button').click()
# возврат в ЛК Учителя по клику лого в шапке
wd.find_element(By.XPATH, '/html/body/div[1]/div/div/a[1]').click()
# закрытие браузера
wd.close()
