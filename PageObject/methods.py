from PageObject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

# loginx= 'wegweg@mail.ru'
# passwordx = 'wegweg@mail.ru'
website = 'https://ts01.shot-uchi.ru/'
# wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')

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

def add_student(cls, surname, name):
        # В классе должен уже быть хотя бы 1 ученик
        wd = cls.wd
        wdw(wd, 10).until(ec.presence_of_element_located(add_student.next)).click()
        wd.find_element(*add_student.add).click()
        wdw(wd, 1).until(ec.presence_of_element_located(add_student.lastname)).send_keys(surname)
        wd.find_element(*add_student.name).send_keys(name)
        wd.find_element(*add_student.sex).click()
        wd.find_element(*add_student.save).click()
