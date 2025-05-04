from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажимаем кнопку, которая открывает новую вкладку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Ждём появления второй вкладки и переключаемся на неё
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Находим значение x и вычисляем результат
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Получаем код из alert
    time.sleep(1)
    alert = browser.switch_to.alert
    print("Результат:", alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()