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
lastnamexx = 'Петрова123'
namexx = 'Настя123'
pswrdxx = 'змн84952'

'''capabilities = {
    "browserName": "chrome",
    "browserVersion": "100",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
} '''


class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        '''cls.wd = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=capabilities)'''
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
        del_student(cls)

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
        # count_msg_1 = len(wd.find_elements(*class_editing.clsedit_phrase1))
        # count_msg_2 = len(wd.find_elements(*class_editing.clsedit_phrase2))
        count_msg_2 = len(wd.find_elements(By.CSS_SELECTOR, '[data-event-info="delete_class"]'))
        # (By.CLASS_NAME, "[class = col-xs-12 mb-10 mt-10]")
        # верный:
        # (By.CSS_SELECTOR, '[data-event-info="delete_class"]')

        # cls.assertTrue(count_msg_1 == 1, 'Пропала фраза-якорь 1')
        cls.assertTrue(count_msg_2 == 1, 'Пропала фраза-якорь 2')

# Кнопка Изменить (редактирование имени, фамилии, итд).
# Есть баг на ts01 шоте, которого нет на продакшене - не удаляется чувак у которого менялся пароль и страница не обновлялась
    def test_06_student_edit(cls):
        wd = cls.wd
        adding_student(cls, surnamex, namex)
        student_editing(cls, lastnamexx, namexx, pswrdxx)
        time.sleep(2)
        count_msg_1 = len(wd.find_elements(*add_student.newpswrd))
        newnamexx = len(wd.find_elements(*add_student.newname))
        cls.assertTrue(count_msg_1 == 1, 'Пароль не изменился')
        cls.assertTrue(newnamexx == 1, 'Имя не изменилось')
        time.sleep(2)
        # del_this_student
        wd.find_element(By.XPATH, "//div[contains(text(),'Настя123')]//..//div[10]//div").click()
        wd.switch_to.alert.accept()
        time.sleep(2)
        # доделать. для последующих тестов чекать что удаляется этот аккаунт. Либо сделать записывать для аасертов рандомную переменную


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()