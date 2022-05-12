from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

class Testing(unittest.TestCase):
    def test_1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element(By.XPATH, "//label[contains(text(), 'First name')]//..//input").send_keys("qwr")
        browser.find_element(By.XPATH, "//label[contains(text(), 'Last name')]//..//input").send_keys("qwr")
        browser.find_element(By.XPATH, "//label[contains(text(), 'Email')]//..//input").send_keys("asf@asdf.ru")
        # Отправляем заполненную форму
        button_click = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Одно из обязательных полей пропало")

    def test_2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element(By.XPATH, "//label[contains(text(), 'First name')]//..//input").send_keys("qwr")
        browser.find_element(By.XPATH, "//label[contains(text(), 'Last name')]//..//input").send_keys("qwr")
        browser.find_element(By.XPATH, "//label[contains(text(), 'Email')]//..//input").send_keys("asf@asdf.ru")
        # Отправляем заполненную форму
        button_click = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Одно из обязательных полей пропало")



if __name__ == "__main__":
    unittest.main()


