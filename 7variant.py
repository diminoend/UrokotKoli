# импорт библиотек
from selenium import webdriver
import time
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#s = Service("C:\\chromedriver\\chromedriver.exe")

""" Flow
- авторизация учителя
- переход в первый классбук из селектора в шапке
- Удаление ученика номер 1g
- добавление нового ученика в класс
- Переход в ЛК
- Закрытие браузера
"""
# Автоматизация через локаторы xpath по тегам с условиями
# создание переменной с вызовом вебдрайвера
wd = webdriver.Chrome("C://chromedriver//chromedriver.exe")
# на весь экран. Чтобы бы был лучше виден мой первый тест:)
wd.maximize_window()
# открытие странички
wd.get('https://ts01.shot-uchi.ru/')
# логин через id
wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
# ввод пароля через xpath
wd.find_element(By.ID, 'password').send_keys('wegweg@mail.ru')
# Доделать. кнопка войти через xpath по слову Войти
wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
# поиск элемента по атрибуту class
time.sleep(1)
wd.find_element(By.XPATH, '//div[contains(@class, "PlateClass")]').click()
# Выбор первого класса в списке
wd.find_element(By.XPATH, "//a[contains(@data-onboarding, 'header-classlist-item-edit')]").click()
# Ждём онбординг 3 секунды, жмём Далее
time.sleep(3)
wd.find_element(By.XPATH, '//div[contains(text(),"Далее")]').click()
# Ищем и удаляем ученика номер 1
wd.find_element(By.XPATH, '//div[contains(text(),"Удалить")][1]').click()
# нажимаем принять во всплывашке
wd.switch_to.alert.accept()
# Жмём кнопку Добавить ученика
wd.find_element(By.XPATH, '//button[contains(text(),"Добавить ученика")]').click()
# ждём 1 секунду появления поля
time.sleep(1)
# Ищем последнее поле Фамилия и вводим - Глав.
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[2]/input").send_keys('Глав')
# вводим Имя - Рыба
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[3]/input").send_keys('Рыба')
# Выбираем Пол - М
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[4]/label[1]").click()
# Жмём кнопку Сохранить
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[10]/button").click()
# возврат в ЛК Учителя по клику лого в шапке
wd.find_element(By.XPATH, "//a[@href='https://ts01.shot-uchi.ru/teachers/stats/main']").click()
# закрытие браузера
wd.close()
