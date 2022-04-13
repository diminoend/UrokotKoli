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

class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)

    def test_01_add_student(cls):
        wd = cls.wd
        wd.find_element(*add_student.add).click()
        wdw(wd, 1).until(ec.presence_of_element_located(add_student.lastname)).send_keys(surnamex)
        wd.find_element(*add_student.name).send_keys(namex)
        wd.find_element(*add_student.sex).click()
        wd.find_element(*add_student.save).click()

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()