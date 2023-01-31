from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))

    x_1 = browser.find_element(By.ID, "num1")
    x_2 = browser.find_element(By.ID, "num2")

    a = int(x_1.text)
    b = int(x_2.text)
    
    y = str(a + b)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"

    # input = browser.find_element(By.ID, "answer")
    #input.send_keys(y)

##########################################

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()