from selenium.webdriver.common.by import By

class locator():
    # https://ts01.shot-uchi.ru/
    login_input = (By.ID, 'login')
    password_input = (By.ID, 'password')
    log_in_button = (By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]')

class lk_main():
    # https://ts01.shot-uchi.ru/teachers/lk/main
    teacherdesk_text = (By.XPATH, '//div[contains(text(),"Учительская доска")]')
    header_class_selector = (By.XPATH, '//div[contains(@class, "PlateClass")]')
    class_add_students = (By.XPATH, "//a[contains(@data-onboarding, 'header-classlist-item-edit')]")
    give_access_parents = (By.XPATH, '//div[contains(text(),"Передайте доступы")]')

class teacher_url():
    lk_url = ('https://ts01.shot-uchi.ru/teachers/lk/main')

class add_student():
    # https://ts01.shot-uchi.ru/signup/teacher/add/students?groupid={id_класса}
    next = (By.XPATH, '//div[contains(text(),"Далее")]')
    add = (By.XPATH, '//button[contains(text(),"Добавить ученика")]')
    lastname = (By.XPATH, "//div[contains(@class, 'styles__Row')]/div/div[2]/input")
    name = (By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[3]/input")
    sex = (By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[4]/label[1]")
    save = (By.XPATH, "//div[contains(@class, 'styles__Row')][last()]/div/div[10]/button")
    change = (By.XPATH, '//div[contains(text(),"Изменить")]')
    delete = (By.XPATH, '//div[contains(text(),"Удалить")]')
    already_invited = (By.XPATH, '//div[contains(text(),"Приглашен")]')
    invite = (By.XPATH, '//div[contains(text(),"Пригласить")]')
    parents_invited = (By.CSS_SELECTOR, "[class*='Invited']")
    prnts_email = (By.CSS_SELECTOR, 'input[name]')
    invite_btn_input = (By.XPATH, "//button[text()='Пригласить']")
    giveacces_btn = (By.XPATH, "//button[text()='Передать доступ']")
    giveaccess_phrase1 = (By.XPATH, "//li[text()='Каждый родитель сможет найти ']")
    giveaccess_phrase2 = (By.XPATH, "//li[text()=' и начните заниматься.']")
    cls_editing = (By.XPATH, "//span[contains(text(),'изменить')]")

class class_editing():
    clsedit_phrase1 = (By.XPATH, '//div[contains(text(),"Редактирование класса")]')
    clsedit_phrase2 = (By.XPATH, "//label[contains(text(),'Программа по предметам:')]")
