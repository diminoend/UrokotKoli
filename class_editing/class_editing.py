# Проверка страницы Редактирования класса -

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'
surnamex = 'Иванов'
namex = 'Костя'
parents_email = 'parents123123123123_123@mail.ru'
lastnamexx = 'Петрова123'
namexx = 'Настя123'
pswrdxx = 'змн84952'

class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located((add_student.next))).click()


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()