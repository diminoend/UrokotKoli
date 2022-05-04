import time
import random
import string
from PageObject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec


# loginx= 'wegweg@mail.ru'
# passwordx = 'wegweg@mail.ru'
website = 'https://ts01.shot-uchi.ru/'
# wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
# surnamex = 'Иванов'
# namex = 'Костя'


def login(wd, loginx, passwordx):
        wd.maximize_window()
        wd.get(website)
        wd.find_element(*locator.login_input).send_keys(loginx)
        wd.find_element(*locator.password_input).send_keys(passwordx)
        wd.find_element(*locator.log_in_button).click()

def selecting_class_in_lk(cls):
        wd = cls.wd
        wdw(wd, 10).until(ec.presence_of_element_located((lk_main.teacherdesk_text)))
        wd.find_element(*lk_main.header_class_selector).click()
        wd.find_element(*lk_main.class_add_students).click()

def onboarding_click(cls):
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located(add_student.next)).click()

def adding_student(cls, surnamex, namex):
        wd = cls.wd
        if len(wd.find_elements(*add_student.change)) >= 1:
                wd.find_element(*add_student.add).click()
                wdw(wd, 1).until(ec.presence_of_element_located(add_student.lastname)).send_keys(surnamex)
                wd.find_element(*add_student.name).send_keys(namex)
                wd.find_element(*add_student.sex).click()
                wd.find_element(*add_student.save).click()
        else:
                wd.find_element(*add_student.lastname).send_keys(surnamex)
                wd.find_element(*add_student.name).send_keys(namex)
                wd.find_element(*add_student.sex).click()
                wd.find_element(*add_student.save).click()

def del_student(cls):
        wd = cls.wd
        wd.find_element(*add_student.delete).click()
        wd.switch_to.alert.accept()

def prnts_invite(self, parents_email):
        wd = self.wd
        wd.find_element(*add_student.invite).click()
        wd.find_element(*add_student.prnts_email).send_keys(parents_email)
        wd.find_element(*add_student.invite_btn_input).click()

def student_editing(cls, lastnamexx, namexx, pswrdxx):
        wd = cls.wd
        wd.find_element(*add_student.change).click()
        wdw(wd, 3).until(ec.presence_of_element_located(add_student.pswrd_hint))
        wd.find_element(*add_student.lastname_change).clear()
        wd.find_element(*add_student.lastname_change).send_keys(lastnamexx)
        wd.find_element(*add_student.name_change).clear()
        wd.find_element(*add_student.name_change).send_keys(namexx)
        wd.find_element(*add_student.sex_change).click()
        wd.find_element(*add_student.pswrd_change).send_keys(pswrdxx)
        wd.find_element(*add_student.btn_save_change).click()

