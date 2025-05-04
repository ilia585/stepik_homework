from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

file_name = "temp.txt"  # объявляем заранее

try:
    # Настройка драйвера Chrome для старой версии selenium
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Открываем страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем поля формы
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Иванов")
    browser.find_element(By.NAME, "email").send_keys("ivan@example.com")

    # Создаём файл и получаем путь
    with open(file_name, "w") as file:
        file.write("Пример текста")

    file_path = os.path.abspath(file_name)

    # Загружаем файл
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Получаем alert
    time.sleep(1)
    alert = browser.switch_to.alert
    print("Результат:", alert.text)
    alert.accept()

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    if os.path.exists(file_name):
        os.remove(file_name)
    time.sleep(5)
    browser.quit()