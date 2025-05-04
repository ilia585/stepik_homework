import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    time.sleep(1)
    final_alert = browser.switch_to.alert
    print(":", final_alert.text)
    final_alert.accept()

finally:
    time.sleep(5)
    browser.quit()