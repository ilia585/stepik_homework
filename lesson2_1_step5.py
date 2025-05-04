import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
     return str(math.log(abs(12 * math.sin(int(x)))))

try:
     browser = webdriver.Chrome()
     browser.get("https://suninjuly.github.io/math.html")

     x_element = browser.find_element(By.ID, "input_value")
     x = x_element.text
     y = calc(x)

     answer_field = browser.find_element(By.ID, "answer")
     answer_field.send_keys(y)

     checkbox = browser.find_element(By.ID, "robotCheckbox")
     checkbox.click()

     radiobutton = browser.find_element(By.ID, "robotsRule")
     radiobutton.click()

     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
     submit_button.click()

     time.sleep(1)
     alert = browser.switch_to.alert
     print("Код для ответа:", alert.text.split()[-1])
     alert.accept()

finally:
     time.sleep(5)
     browser.quit()
