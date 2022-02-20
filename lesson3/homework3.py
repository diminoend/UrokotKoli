# импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import unittest, time
'''
- тест логина учителя
- тест выбора класса из селектора в шапке
- тест удаления ученика
- тест добавления ученика
'''
class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        cls.wd.get('https://ts01.shot-uchi.ru/')

    def test_login(self):
        wd = self.wd
        login = wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
        password = wd.find_element(By.ID, 'password').send_keys('wegweg@mail.ru')
        log_in = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
        time.sleep(1)
        self.assertEqual('https://ts01.shot-uchi.ru/teachers/lk/main', wd.current_url, 'ЛК не прогрузился')

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()