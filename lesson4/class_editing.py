# Проверка страницы Редактирования класса - https://ts01.shot-uchi.ru/signup/teacher/add/students?groupid={id_класса}

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

class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, loginx, passwordx)
        selecting_class_in_lk(cls)
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located((add_student.next))).click()

# Добавление студента
    def test_01_adding_student(cls):
        wd = cls.wd
        count_del_word_1 = len(wd.find_elements(*add_student.change))
        adding_student(cls, surnamex, namex)
        time.sleep(2)
        count_del_word_2 = len(wd.find_elements(*add_student.change))
        cls.assertTrue(count_del_word_1 < count_del_word_2, 'Студент не добавился')

# Удаление студента
    def test_02_deleting_student(cls):
        wd = cls.wd
        adding_student(cls, surnamex, namex)
        time.sleep(2)
        count_del_word_1 = len(wd.find_elements(*add_student.change))
        del_student(cls)
        time.sleep(2)
        count_del_word_2 = len(wd.find_elements(*add_student.change))
        cls.assertTrue(count_del_word_1 > count_del_word_2, 'Студент не удалился')

# Приглашение родителя. Добавляем и удаляем студентов, т.к. уже могут быть все приглашены
    def test_03_invite(cls):
        wd = cls.wd
        count_invite_1 = len(wd.find_elements(*add_student.parents_invited))
        adding_student(cls, surnamex, namex)
        prnts_invite(cls, parents_email)
        # wdw(wd, 10).until(ec.presence_of_element_located(add_student.parents_invited))
        time.sleep(2)
        count_invite_2 = len(wd.find_elements(*add_student.parents_invited))
        cls.assertTrue(count_invite_1 < count_invite_2, 'Приглашение не отправлено')
        time.sleep(2)
        del_student(cls)

# Кнопка Передать доступ
    def test_04_give_access(cls):
        wd = cls.wd
        wd.find_element(*add_student.giveacces_btn).click()
        wdw(wd, 10).until(ec.presence_of_element_located(add_student.giveaccess_phrase1))
        count_msg_1 = len(wd.find_elements(*add_student.giveaccess_phrase1))
        count_msg_2 = len(wd.find_elements(*add_student.giveaccess_phrase2))
        cls.assertTrue(count_msg_1 == 1, 'Пропала фраза-якорь 1')
        cls.assertTrue(count_msg_2 == 1, 'Пропала фраза-якорь 2')

# Кнопка Изменить (переход в редактирование предметов класса)
    def test_05_class_edit(cls):
        wd = cls.wd
        wd.find_element(*add_student.cls_editing).click()
        wdw(wd, 10).until(ec.presence_of_element_located(class_editing.clsedit_phrase1))
        # time.sleep(2)
        count_msg_1 = len(wd.find_elements(*class_editing.clsedit_phrase1))
        count_msg_2 = len(wd.find_elements(*class_editing.clsedit_phrase2))
        cls.assertTrue(count_msg_1 == 1, 'Пропала фраза-якорь 1')
        cls.assertTrue(count_msg_2 == 1, 'Пропала фраза-якорь 2')


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()