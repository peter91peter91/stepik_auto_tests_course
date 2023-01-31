from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
##########################################
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
  
    image_x  = browser.find_element(By.ID, "treasure")  
    # x_element=image_x.text  //это не сработает . так как там не текст а атрибут
    x_element = image_x.get_attribute("valuex")
    y = calc(x_element)
    
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

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(3)

    # находим элемент, содержащий текст
 #   welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
 #   welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
  #  assert "Congratulations! You have successfully registered!" == welcome_text
  #  print(" УСПЕХ ")
    
        
#except  (IOError,Exception) as e:
#    print("произошла какая-то ошибка....")
#    print(e)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()