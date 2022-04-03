from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'
surname = 'Иванов'
name = 'Костя'

class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')

    def test_01_selecting_class(cls):
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)

    def test_02_add_student(cls):
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)
        add_student(surname, name)

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()