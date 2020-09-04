from selenium import webdriver

import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn_el = browser.find_element_by_name("firstname")
    fn_el.send_keys("AAA")

    ln_el = browser.find_element_by_name("lastname")
    ln_el.send_keys("AAA")

    em_el = browser.find_element_by_name("email")
    em_el.send_keys("AAA")

    f_input = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
     
    f_input.send_keys(file_path)

    submit_el = browser.find_element_by_css_selector("button[type='submit']")
    submit_el.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
