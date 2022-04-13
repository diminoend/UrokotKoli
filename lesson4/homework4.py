from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'

class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, loginx, passwordx)

    def test_01_login(cls):
        # авторизация под Учителем
        wd = cls.wd
        wdw(wd, 10).until(ec.presence_of_element_located((lk_main.teacherdesk_text)))
        b = wd.current_url
        cls.assertEqual(teacher_url.lk_url, b, 'Teacher desk not loaded')

    def test_02_selecting_class(cls):
        wd = cls.wd
        wd.find_element(*lk_main.header_class_selector).click()
        wd.find_element(*lk_main.class_add_students).click()
        cls.assertTrue((wdw(wd, 3).until(ec.presence_of_element_located(
            (lk_main.give_access_parents)))), 'Anchor not found "Передайте доступы"')

    def test_03_add_student(cls):
        # В классе должен уже быть хотя бы 1 ученик
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located(add_student.next)).click()
        wd.find_element(*add_student.add).click()
        wdw(wd, 1).until(ec.presence_of_element_located(add_student.lastname)).send_keys('Иванов')
        wd.find_element(*add_student.name).send_keys('Костя')
        wd.find_element(*add_student.sex).click()
        wd.find_element(*add_student.save).click()
        # Следующий тест проверяет что есть кнопка Удалить, которая появляется только при наличии ученика

    def test_04_deleting_student(cls):
        wd = cls.wd
        # ждём 3 секунды для того чтобы появился только что добавленный ученик
        time.sleep(3)
        a = len(wd.find_elements(*add_student.change))
        # По кнопке Изменить смотрим количество учеников. Количество "Изменить" = количеству учеников
        wd.find_element(*add_student.delete).click()
        wd.switch_to.alert.accept()
        # Снова считаем сколько стало Изменить:
        time.sleep(2)
        b = len(wd.find_elements(*add_student.change))
        cls.assertTrue(a > b, 'Студент не удалился')


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()