from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome('C://chromedriver//chromedriver.exe')
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# закрываем браузер после всех манипуляций
browser.quit()
'''
class teacher(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, login=loginx, password=passwordx)

    def test_login(cls):
        # авторизация под Учителем
        wd = cls.wd
        wdw(wd, 10).until(ec.presence_of_element_located((lk_main.teacherdesk_text)))
        b = wd.current_url
        cls.assertEqual(teacher_url.lk_url, b, 'Teacher desk not loaded')

    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()'''