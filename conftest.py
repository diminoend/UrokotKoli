from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest
from PageObject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

website = 'https://ts01.shot-uchi.ru/'
loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'

@pytest.fixture(autouse=True)
def preconditions():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(website)
    browser.find_element(*locator.login_input).send_keys(loginx)
    browser.find_element(*locator.password_input).send_keys(passwordx)
    browser.find_element(*locator.log_in_button).click()
    wdw(browser, 10).until(ec.presence_of_element_located((lk_main.teacherdesk_text)))
    browser.find_element(*lk_main.header_class_selector).click()
    browser.find_element(*lk_main.class_add_students).click()
    wdw(browser, 3).until(ec.presence_of_element_located(add_student.next)).click()
    yield browser
    browser.quit()
