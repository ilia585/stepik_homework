import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Вычисляем текст ссылки
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))  # Результат: "230000"

try:
    # Настройка ChromeDriver с автоматической установкой
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    
    # Находим и кликаем зашифрованную ссылку
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    time.sleep(1)  # Небольшая задержка для загрузки
    
    # Заполняем форму
    browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    
    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
     
    # Получаем код из алерта
    alert = browser.switch_to.alert
    code = alert.text.split()[-1]
    print(f"Проверочный код: {code}")
    alert.accept()

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    if 'browser' in locals():
        time.sleep(5)
        browser.quit()
