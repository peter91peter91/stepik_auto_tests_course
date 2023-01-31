from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time
import math
import os 

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

##########################################
# говорим Selenium проверять в течение 1 секунд, пока текст не станет 100
    price_x = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element ((By.ID, "price"), "100")   )
    
    if price_x == True:        #  False - не сработает!  всё гудик
        # Отправляем заполненную форму
        button = browser.find_element(By.ID, "book")
        button.click()
    

    browser.execute_script("window.scrollBy(0, 100)");
##########################################
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = (browser.find_element(By.ID, "input_value")).text    
    y = calc(x_element)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
    
    time.sleep(2)

##########################################
    # Копирование числа из алерта в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

##########################################
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()