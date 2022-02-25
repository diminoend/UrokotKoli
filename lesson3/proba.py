def test_04_deleting_student(self):
    wd = self.wd
    first_len = len(wd.find_elements(By.XPATH, '//div[contains(text(),"Изменить")]'))
    # ждём 3 секунды для того чтобы появился только что добавленный ученик
    wdw(wd, 1).until(ec.presence_of_element_located(len((wd.find_elements
                                                         (By.XPATH, '//div[contains(text(),"Изменить")]') + 1))
    # По кнопке Изменить смотрим количество учеников. Количество "Изменить" = количеству учеников
    a = len((wd.find_elements(By.XPATH, '//div[contains(text(),"Изменить")]') + 1)
    # print(str(a) + " учеников")
    wd.find_element(By.XPATH, '//div[contains(text(),"Удалить")]').click()
    wd.switch_to.alert.accept()
    # Снова считаем сколько стало Изменить
    time.sleep(2)
    b = len(wd.find_elements(By.XPATH, '//div[contains(text(),"Изменить")]'))
    self.assertTrue(a > b, 'Студент не удалился')