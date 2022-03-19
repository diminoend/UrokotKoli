from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'
website = 'https://ts01.shot-uchi.ru/'
# wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')

def login(wd, login, password):
        wd.maximize_window()
        wd.get(website)
        login = wd.find_element(By.ID, 'login').send_keys(loginx)
        password = wd.find_element(By.ID, 'password').send_keys(passwordx)
        log_in = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
        # wdw(wd, 3).until(ec.presence_of_element_located(
        #        (By.XPATH, '//div[contains(text(),"Учительская доска")]')))
        # b = wd.current_url
        # self.assertEqual('https://ts01.shot-uchi.ru/teachers/lk/main', b, 'ЛК не прогрузился')

# login(wd, loginx, passwordx)