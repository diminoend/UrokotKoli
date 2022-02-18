#импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC




wd = webdriver.Chrome("C://chromedriver//chromedriver.exe") #переменная с вебдрайвером
#wd.implicitly_wait(10) #неявное ожидание с глобальным таймером 10 сек

wd.get('https://uchi.ru/') #открытие учи ру

#поиск и взаимодействие с полем ввода логина с явным ожиданием
login = wdw(wd,3).until(EC.presence_of_element_located((By.ID,'login'))).send_keys('login')

#поиск и взаимодействие с полем ввода пароля с явным ожиданием
password = wdw(wd,3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div[2]/div/form/div[2]/input'))).send_keys('password')

#создание переменной с селектором кнопки войти через xpath
log_in = wd.find_element_by_xpath('/html/body/main/section/div[2]/div/form/input[4]')

#клик по кнопке войти
log_in.click()


main_page = 'https://uchi.ru/students/main' #переменная со статичным урлом
current_url = wd.current_url #берём текущий урл странички

assert current_url == main_page, 'wrong url' #ассерт с проверкой текущего урла

wd.close() #закрытие браузера