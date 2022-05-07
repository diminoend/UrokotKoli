from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'
br = webdriver.Chrome(executable_path=ChromeDriverManager().install())

try:
    br.get(link)
    br.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("w23")
    br.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("w23")
    br.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("w23")

    element = br.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'qwe3.txt')
    element.send_keys(file_path)

    br.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(5)
    br.quit()

