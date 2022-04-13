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
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located((add_student.next))).click()

    def test_01_adding_student(cls):
        wd = cls.wd
        count_del_word_1 = len(wd.find_elements(*add_student.change))
        adding_student(cls, surnamex, namex)
        time.sleep(2)
        count_del_word_2 = len(wd.find_elements(*add_student.change))
        cls.assertTrue(count_del_word_1 < count_del_word_2, 'Студент не добавился')

    def test_02_deleting_student(cls):
        wd = cls.wd
        count_del_word_1 = len(wd.find_elements(*add_student.change))
        del_student(cls)
        time.sleep(2)
        count_del_word_2 = len(wd.find_elements(*add_student.change))
        cls.assertTrue(count_del_word_1 > count_del_word_2, 'Студент не удалился')

    def test_03_invite(cls):
        wd = cls.wd
        if len(*add_student.already_invited) != 0:
            wd.find_element(*add_student.invite).click()


        # print(len(wd.find_elements(By.XPATH, '//div[contains(text(),"Приглашен")]')))


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()