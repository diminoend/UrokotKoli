from selenium import webdriver
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

    def test_01_success_login(cls):
        # авторизация под Учителем
        wd = cls.wd
        wdw(wd, 10).until(ec.presence_of_element_located((lk_main.teacherdesk_text)))
        b = wd.current_url
        cls.assertEqual(teacher_url.lk_url, b, 'Teacher desk not loaded')

    def test_02_selecting_class(cls):
        wd = cls.wd


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()