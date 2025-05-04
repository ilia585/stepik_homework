from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Поиск всех полей ввода на странице
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполнение каждого поля текстом "Мой ответ"
    for element in elements:
        element.send_keys("Мой ответ")

    # Поиск и нажатие кнопки отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание 30 секунд для копирования кода из alert
    time.sleep(30)
    # Закрытие браузера
    browser.quit()
