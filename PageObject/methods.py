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


def adding_student(self, browser, surnamex, namex):
    if len(browser.find_elements(*add_student.change)) >= 1:
        browser.find_element(*add_student.add).click()
        wdw(browser, 1).until(ec.presence_of_element_located(add_student.lastname)).send_keys(surnamex)
        browser.find_element(*add_student.name).send_keys(namex)
        browser.find_element(*add_student.sex).click()
        browser.find_element(*add_student.save).click()
    else:
        browser.find_element(*add_student.lastname).send_keys(surnamex)
        browser.find_element(*add_student.name).send_keys(namex)
        browser.find_element(*add_student.sex).click()
        browser.find_element(*add_student.save).click()
    return self


def del_student(self, browser):
    browser.find_element(*add_student.delete).click()
    browser.switch_to.alert.accept()
    return self


def prnts_invite(self, browser, parents_email):
    browser.find_element(*add_student.invite).click()
    browser.find_element(*add_student.prnts_email).send_keys(parents_email)
    browser.find_element(*add_student.invite_btn_input).click()
    return self


def student_editing(self, browser, lastnamexx, namexx, pswrdxx):
    browser.find_element(*add_student.change).click()
    wdw(browser, 3).until(ec.presence_of_element_located(add_student.pswrd_hint))
    browser.find_element(*add_student.lastname_change).clear()
    browser.find_element(*add_student.lastname_change).send_keys(lastnamexx)
    browser.find_element(*add_student.name_change).clear()
    browser.find_element(*add_student.name_change).send_keys(namexx)
    browser.find_element(*add_student.sex_change).click()
    browser.find_element(*add_student.pswrd_change).send_keys(pswrdxx)
    browser.find_element(*add_student.btn_save_change).click()
    return self
