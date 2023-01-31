from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

import os 
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    elements = browser.find_elements(By.XPATH, "//input")
    
    print("начало FOR")
    i=1
    for element in elements:  
        if i in range (1,4):
            print(i)
            element.send_keys("12345")
            i = i + 1  


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "new.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    #browser.find_element(By.ID, "file")

    #for i in range(1,4): #от 1 до 3

    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))

    #x_element = (browser.find_element(By.ID, "input_value")).text    
    #y = calc(x_element)
    
    #browser.execute_script("window.scrollBy(0, 100)");
    
    #input = browser.find_element(By.ID, "answer")
    #input.send_keys(y)

    #option1 = browser.find_element(By.ID, "robotCheckbox")
    #option1.click()
    
    #option2 = browser.find_element(By.ID, "robotsRule")
    #option2.click()

##########################################

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()