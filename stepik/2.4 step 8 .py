import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
#ghghgk

link = 'http://suninjuly.github.io/explicit_wait2.html'
br = webdriver.Chrome(executable_path=CDM().install())

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    br.get(link)
    wait = WDW(br, 15).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    btn_Book = br.find_element(By.CSS_SELECTOR, "[onclick='checkPrice();']").click()

    x = br.find_element(By.ID, 'input_value').text
    y = calc(x)

    br.find_element(By.ID, 'answer').send_keys(y)
    br.find_element(By.ID, 'solve').click()


finally:
    time.sleep(5)
    br.quit()
