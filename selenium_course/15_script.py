from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

import os 
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
##########################################
  
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = (browser.find_element(By.ID, "input_value")).text    
    y = calc(x_element)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

##########################################
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()