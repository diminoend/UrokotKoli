from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'

# НЕПРАВИЛЬНАЯ ЛОГИКА. НЕ ИСПОЛЬЗОВАТЬ!!!!!!!!!!!!!!!!!

class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')

    def test_01_selecting_class(asd):
        login(asd.wd, loginx, passwordx)
        selecting_class_in_lk(asd)

    def test_02_add_student(cls):
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)
        add_student()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()