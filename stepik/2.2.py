
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    br = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    br.get(link)

    num1 = br.find_element(By.ID, 'num1').text
    num2 = br.find_element(By.ID, 'num2').text
    x = str(int(num1) + int(num2))

    select = Select(br.find_element(By.ID, 'dropdown'))
    select.select_by_value(x)

    br.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(1)
    br.quit()

