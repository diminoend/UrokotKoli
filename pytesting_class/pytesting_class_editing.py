# Проверка страницы Редактирования класса - https://ts01.shot-uchi.ru/signup/teacher/add/students?groupid={id_класса}

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import time

import pytest

surnamex = 'Иванов'
namex = 'Костя'
parents_email = 'parents123123123123_123@mail.ru'
lastnamexx = 'Петрова123'
namexx = 'Настя123'
pswrdxx = 'змн84952'
# link = 'https://ts01.shot-uchi.ru/'

# website = 'https://ts01.shot-uchi.ru/'
# loginx = 'wegweg@mail.ru'
# passwordx = 'wegweg@mail.ru'


class Test_Class_editing:
    def test_01_add_student(self, browser):
        count_del_word_1 = len(browser.find_elements(*add_student.change))
        adding_student(self, browser, surnamex, namex)
        time.sleep(2)
        count_del_word_2 = len(browser.find_elements(*add_student.change))
        assert count_del_word_1 < count_del_word_2, 'Student has not add'
        del_student(self, browser)

    def test_02_del_student(self, browser):
        adding_student(self, browser, surnamex, namex)
        time.sleep(2)
        count_del_word_1 = len(browser.find_elements(*add_student.change))
        del_student(self, browser)
        time.sleep(2)
        count_del_word_2 = len(browser.find_elements(*add_student.change))
        assert count_del_word_1 > count_del_word_2, 'Student has not delete'

    # Add and delete students, because all already may be invited
    def test_03_parents_inviting(self, browser):
        adding_student(self, browser, surnamex, namex)
        prnts_invite(self, browser, parents_email)
        browser.find_element(*add_student.invite).click()
        # Текст в модале - Приглашение отправлено
        assert len(browser.find_elements(*add_student.already_invited)) == 1, "Приглашение не отправлено"
        browser.find_element(*add_student.another_prnts_mail_close).click()
        del_student(self, browser)
        time.sleep(3)

    # Give access to parents button
    def test_04_give_access(self, browser):
        browser.find_element(*add_student.giveacces_btn).click()
        wdw(browser, 10).until(ec.presence_of_element_located(add_student.giveaccess_phrase1))
        count_msg_1 = len(browser.find_elements(*add_student.giveaccess_phrase1))
        count_msg_2 = len(browser.find_elements(*add_student.giveaccess_phrase2))
        assert count_msg_1 == 1, 'Пропала фраза-якорь 1'
        assert count_msg_2 == 1, 'Пропала фраза-якорь 2'


    # Кнопка Изменить (переход в редактирование предметов класса)
    def test_05_class_edit(self, browser):
        browser.find_element(*add_student.cls_editing).click()
        wdw(browser, 10).until(ec.presence_of_element_located(class_editing.clsedit_phrase1))
        # time.sleep(2)
        count_msg_1 = len(browser.find_elements(*class_editing.clsedit_phrase1))
        count_msg_2 = len(browser.find_elements(*class_editing.clsedit_phrase2))
        count_msg_3 = len(browser.find_elements(By.CSS_SELECTOR, '[data-event-info="delete_class"]'))
        assert count_msg_1 == 1, 'Пропала фраза-якорь 1'
        assert count_msg_2 == 1, 'Пропала фраза-якорь 2'
        assert count_msg_3 == 1, 'Пропала фраза-якорь 3'

    # Кнопка Изменить (редактирование имени, фамилии, итд).
    def test_06_student_edit(self, browser):
        adding_student(self, browser, surnamex, namex)
        student_editing(self, browser, lastnamexx, namexx, pswrdxx)
        time.sleep(2)
        count_msg_1 = len(browser.find_elements(*add_student.newpswrd))
        newnamexx = len(browser.find_elements(*add_student.newname))
        assert count_msg_1 == 1, 'Password has not change'
        assert newnamexx == 1, 'Name has not change'
        time.sleep(2)
        # delete this student
        browser.find_element(By.XPATH, "//div[contains(text(),'Настя123')]//..//div[10]//div").click()
        browser.switch_to.alert.accept()
        time.sleep(2)

'''
    # Проверка того что при отправленном приглашении, в модале можно отправить приглос на другую почту
    def test_07_another_prnts_mail(self, browser):
        adding_student(self, browser, surnamex, namex)
        prnts_invite(self, browser, parents_email)
        invite_btn = browser.find_element(*add_student.invite).click()
        browser.find_element(add_student.another_prnts_mail).click()
        browser.find_element(add_student.prnts_email).send_keys(parents_email)
        browser.find_element(add_student.invite_btn_input).click()
        invite_btn.click()

        # del_student(self, browser)
        time.sleep(3)

    # Родитель принял приглашение
'''
