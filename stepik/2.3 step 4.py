from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'
br = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    br.get(link)
    br.find_element(By.CLASS_NAME, "btn").click()
    confirm = br.switch_to.alert
    confirm.accept()

    x = br.find_element(By.ID, 'input_value').text
    y = calc(x)

    br.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
    br.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(5)
    br.quit()


