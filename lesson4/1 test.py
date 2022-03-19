# импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, login=loginx, password=passwordx)

    def test_01_login(cls):
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"Учительская доска")]')))
        b = wd.current_url
        cls.assertEqual('https://ts01.shot-uchi.ru/teachers/lk/main', b, 'ЛК не прогрузился')

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()