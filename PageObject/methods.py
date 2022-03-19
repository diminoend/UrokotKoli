
from PageObject.locators import *

loginx = 'wegweg@mail.ru'
passwordx = 'wegweg@mail.ru'
website = 'https://ts01.shot-uchi.ru/'
# wd = webdriver.Chrome('C://chromedriver//chromedriver.exe')

def login(wd, login, password):
        wd.maximize_window()
        wd.get(website)
        login = wd.find_element(*locator.login_input).send_keys(loginx)
        password = wd.find_element(*locator.password_input).send_keys(passwordx)
        log_in = wd.find_element(*locator.log_in_button).click()

# login(wd, loginx, passwordx)