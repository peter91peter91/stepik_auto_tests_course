from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# только обязательные поля, отмеченные символом *: First name, last name, email.

   # input1 = browser.find_element(By.TAG_NAME, "input")
    input1 = browser.find_element(By.CLASS_NAME, "form-control.first")   
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")   
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")  
    input3.send_keys("your_email")
   # input4 = browser.find_element(By.ID, "country")
   # input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//div//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла