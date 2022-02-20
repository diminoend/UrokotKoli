#импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
import unittest, time

#создаём класс с тестами где мы наследуем функции из юниттеста
class login_checking(unittest.TestCase):
    #используем  декоратор класс метод чтобы было видно, что это метод класса.
    @classmethod
    #создаём функцию SetUpClass в которой определяем вебдрайвер
    #и открываем страничку - данная настройка применяется ко всем тестам в самом начале запуска
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('/Users/nikolaev/Desktop/Autotest/education/chromedriver')
        cls.wd.get('https://uchi.ru/')

    #создаём функцию с тестом, название функции с тестом всегда должно начинаться с test или unittest её не увидит
    def test_01_login(self):
        #переопределяем вебдрайвер
        wd = self.wd
        login = wdw(wd, 3).until(EC.presence_of_element_located((By.ID, 'login')),'missing login input').send_keys('login')
        password = wdw(wd, 3).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/section/div[2]/div/form/div[2]/input'))).send_keys('password')
        log_in = wd.find_element_by_xpath('/html/body/main/section/div[2]/div/form/input[4]')
        log_in.click()

    #создаём второй тест
    def test_02_url_check(self):
        wd = self.wd
        main_page = 'https://uchi.ru/students/main'  # переменная со статичным урлом
        current_url = wd.current_url  # берём текущий урл странички
        assert current_url == main_page, 'wrong url'  # ассерт с проверкой текущего урла

    #создаём функцию tearDownClass в которой закрываем браузер
    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()