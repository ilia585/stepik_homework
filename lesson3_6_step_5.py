# Задание: авторизация на сайте
import time
import config
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_authorization(browser):
    browser.get('https://stepik.org/lesson/236895/step/1')
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.NAME, 'login').send_keys(config.login)
    browser.find_element(By.NAME, 'password').send_keys(config.passw)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
    # WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-dialog-inner')))
    time.sleep(5)