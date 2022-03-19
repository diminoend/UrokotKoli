from selenium.webdriver.common.by import By

class locator():
    login_input = (By.ID, 'login')
    password_input = (By.ID, 'password')
    log_in_button = (By.XPATH, '/html/body/main/section/div[2]/div/form/input[4]')
