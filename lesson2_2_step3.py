import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    # Находим числа для суммы
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # Вычисляем сумму
    total = int(num1) + int(num2)

    # Выбираем сумму в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(total))

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Выводим алерт с результатом
    time.sleep(1)
    alert = browser.switch_to.alert
    print("Код для ответа:", alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()