# импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import unittest, time
'''
- тест логина учителя
- тест выбора класса из селектора в шапке
- тест добавления ученика
- тест удаления ученика
'''
class teacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')
        cls.wd.maximize_window()
        cls.wd.get('https://ts01.shot-uchi.ru/')

    def test_01_login(self):
        wd = self.wd
        login = wd.find_element(By.ID, 'login').send_keys('wegweg@mail.ru')
        password = wd.find_element(By.ID, 'password').send_keys('wegweg@mail.ru')
        log_in = wd.find_element(By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]').click()
        wdw(wd, 3).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"Учительская доска")]')))
        b = wd.current_url
        self.assertEqual('https://ts01.shot-uchi.ru/teachers/lk/main', b, 'ЛК не прогрузился')

    def test_02_selecting_class(self):
        wd = self.wd
        wd.find_element(By.XPATH, '//div[contains(@class, "PlateClass")]').click()
        wd.find_element(By.XPATH, "//a[contains(@data-onboarding, 'header-classlist-item-edit')]").click()
        self.assertTrue((wdw(wd, 3).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"Передайте доступы")]')))), 'Не найден якорь "Передайте доступы"')

    def test_03_add_student(self):
        # В классе должен уже быть хотя бы 1 ученик
        wd = self.wd
        # ожидание и клик по Далее в онбординге
        wdw(wd, 3).until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(),"Далее")]'))).click()
        wd.find_element(By.XPATH, '//button[contains(text(),"Добавить ученика")]').click()
        wdw(wd, 1).until(ec.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'styles__Row')]/div/div[2]/input"))).send_keys('Иванов')
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[3]/input").send_keys('Костя')
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[4]/label[1]").click()
        wd.find_element(By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[10]/button").click()
        # Следующий тест проверяет что есть кнопка Удалить, которая появляется только при наличии ученика

    def test_04_deleting_student(self):
        wd = self.wd
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
        self.assertTrue(a > b, 'Студент не удалился')


    @classmethod
    def tearDownClass(cls):
        cls.wd.close()

if __name__ == "__main__":
    unittest.main()