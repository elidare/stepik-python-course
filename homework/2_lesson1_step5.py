from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_el = browser.find_element_by_id("input_value")
    x = num_el.text

    time.sleep(1)
    y = calc(x)

    input_el = browser.find_element_by_id("answer")
    input_el.send_keys(y)

    time.sleep(1)

    #Отметить checkbox "I'm the robot".
    chk_el = browser.find_element_by_id("robotCheckbox")
    chk_el.click()

    time.sleep(1)

    #Выбрать radiobutton "Robots rule!".
    rdbtn_el = browser.find_element_by_id("robotsRule")
    rdbtn_el.click()

    time.sleep(1)

    #Нажать на кнопку Submit.
    submit_el = browser.find_element_by_css_selector("button[type='submit']")
    submit_el.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
