from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    elements1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    elements2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    x = int(elements1.text)
    y = int(elements2.text)
    summ = x + y
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()