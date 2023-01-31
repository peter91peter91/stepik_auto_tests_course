from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    # Ваш код, который заполняет обязательные поля
    # только обязательные поля, отмеченные символом *: First name, last name, email.

    input1 = browser.find_element(By.XPATH, "//div[1]/div[1]/input")
    input1.send_keys("Ivan")
    
    try:
        input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']//following-sibling::input")
        input2.send_keys("Petrov")
        print("1)ФОРМОЧКА ФАМИЛИИ УСПЕШНО НАЙДЕНА И ЗАПОЛНЕНА")    
    finally: pass  
        
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("your_email")

    # button = browser.find_element(By.XPATH, "//div//button[text()='Submit']")
    # button.click()
##########################################

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
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("2)РЕГИСТРАЦИЯ УСПЕШНО ПРОЙДЕНА")
    
        
#except  (IOError,Exception) as e:
#    print("произошла какая-то ошибка....")
#    print(e)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()