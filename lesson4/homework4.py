# импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from PageObject.methods import *
from PageObject.locators import *
import unittest, time

class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        login(cls.wd, login=loginx, password=passwordx)

    def test_01_login(cls):
        wd = cls.wd
        wdw(wd, 3).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"Учительская доска")]')))
        b = wd.current_url
        cls.assertEqual('https://ts01.shot-uchi.ru/teachers/lk/main', b, 'ЛК не прогрузился')

    def test_02_selecting_class(cls):
        wd = cls.wd
        wd.find_element(By.XPATH, '//div[contains(@class, "PlateClass")]').click()
        wd.find_element(By.XPATH, "//a[contains(@data-onboarding, 'header-classlist-item-edit')]").click()
        cls.assertTrue((wdw(wd, 3).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"Передайте доступы")]')))), 'Не найден якорь "Передайте доступы"')

    def test_03_add_student(cls):
        # В классе должен уже быть хотя бы 1 ученик
        wd = cls.wd
        # ожидание и клик по Далее в онбординге
        wdw(wd, 3).until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(),"Далее")]'))).click()
        wd.find_element(By.XPATH, '//button[contains(text(),"Добавить ученика")]').click()
        wdw(wd, 1).until(ec.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'styles__Row')]/div/div[2]/input"))).send_keys('Иванов')
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[3]/input").send_keys('Костя')
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[4]/label[1]").click()
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[10]/button").click()
        # Следующий тест проверяет что есть кнопка Удалить, которая появляется только при наличии ученика

    def test_04_deleting_student(cls):
        wd = cls.wd
        # ждём 3 секунды для того чтобы появился только что добавленный ученик
        time.sleep(3)
        # По кнопке Изменить смотрим количество учеников. Количество "Изменить" = количеству учеников
        a = len(wd.find_elements(By.XPATH, '//div[contains(text(),"Изменить")]'))
        # print(str(a) + " учеников")
        wd.find_element(By.XPATH, '//div[contains(text(),"Удалить")]').click()
        wd.switch_to.alert.accept()
        # Снова считаем сколько стало Изменить
        time.sleep(2)
        b = len(wd.find_elements(By.XPATH, '//div[contains(text(),"Изменить")]'))
        cls.assertTrue(a > b, 'Студент не удалился')


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()