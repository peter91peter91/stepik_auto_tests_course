from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

import os 
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
##########################################
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
  
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = (browser.find_element(By.ID, "input_value")).text    
    y = calc(x_element)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    time.sleep(2)
##########################################
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()