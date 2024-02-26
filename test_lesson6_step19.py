from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class TestAbs(unittest.TestCase):
    def test_abs_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(1) > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > input")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(("Congratulations! You have successfully registered!"), welcome_text, "Should be absolute value of a number")
        
    def test_abs_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(1) > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > input")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(("Congratulations! You have successfully registered!"), \
        welcome_text, "Should be absolute value of a number")



if __name__ == "__main__":
    pytest.main()