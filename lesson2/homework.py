# импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import time

# создание переменной с вызовом вебдрайвера
wd = webdriver.Chrome("C://chromedriver//chromedriver.exe")
# на весь экран
wd.maximize_window()
# открытие странички
wd.get('https://ts01.shot-uchi.ru/')

# логин
wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
# ввод пароля
wd.find_element(By.ID, 'password').send_keys('wegweg@mail.ru')
# Доделать. кнопка войти через xpath по слову Войти
wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()

# Неявное ожидание селектора переключения классов в шапке
wdw(wd,3).until(ec.presence_of_element_located((By.XPATH, '//div[contains(@class, "PlateClass")]'))).click()

# Выбор первого класса в списке
wd.find_element(By.XPATH, "//a[contains(@data-onboarding, 'header-classlist-item-edit')]").click()

#Неявное ожидание онбординга 3 секунды, жмём Далее
wdw(wd,3).until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(),"Далее")]'))).click()

# Ищем и удаляем ученика номер 1
wd.find_element(By.XPATH, '//div[contains(text(),"Удалить")][1]').click()
# нажимаем принять во всплывашке
wd.switch_to.alert.accept()
# Жмём кнопку Добавить ученика
wd.find_element(By.XPATH, '//button[contains(text(),"Добавить ученика")]').click()

# Неявное ожидание 1 сек поля Фамилия, добавление - Глав
wdw(wd,1).until(ec.presence_of_element_located(
    (By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[2]/input"))).send_keys('Глав')

# вводим Имя - Рыба
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[3]/input").send_keys('Рыба')
# Выбираем Пол - М
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[4]/label[1]").click()
# Жмём кнопку Сохранить
wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[10]/button").click()
# возврат в ЛК Учителя по клику лого в шапке
wd.find_element(By.XPATH, "//a[@href='https://ts01.shot-uchi.ru/teachers/stats/main']").click()

time.sleep(1)
a = "https://ts01.shot-uchi.ru/teachers/lk/main"
b = wd.current_url
assert a == b

# закрытие браузера
wd.close()