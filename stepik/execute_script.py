
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import math



link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    br = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    br.get(link)

    x = br.find_element(By.ID, 'input_value').text
    y = calc(x)

    br.find_element(By.ID, 'answer').send_keys(y)
    rbtchek = br.find_element(By.ID, 'robotCheckbox')
    br.execute_script("return arguments[0].scrollIntoView(true);", rbtchek)
    rbtchek.click()
    br.find_element(By.ID, 'robotsRule').click()
    btn = br.find_element(By.CLASS_NAME, 'btn')
    br.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()



finally:
    time.sleep(5)
    br.quit()

