from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = (browser.find_element(By.ID, "input_value")).text    
    y = calc(x_element)
    
    browser.execute_script("window.scrollBy(0, 100)");
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

##########################################

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()