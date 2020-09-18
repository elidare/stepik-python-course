from selenium import webdriver

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_el = browser.find_element_by_id("input_value")
    x = num_el.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input_el = browser.find_element_by_id("answer")
    input_el.send_keys(y)

    chk_el = browser.find_element_by_id("robotCheckbox")
    chk_el.click()

    rdbtn_el = browser.find_element_by_id("robotsRule")
    rdbtn_el.click()

    submit_el = browser.find_element_by_css_selector("button[type='submit']")
    submit_el.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
