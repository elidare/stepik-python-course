from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
  def test_registration1(self):
    browser = webdriver.Chrome()
    browser.get(link1)

    input_first_name = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
    input_first_name.send_keys("AAA")

    input_last_name = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
    input_last_name.send_keys("AAA")

    input_email = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
    input_email.send_keys("AAA")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    self.assertEqual("Congratulations! You have successfully registered!", \
      welcome_text, "Should be same registration text")

  def test_registration2(self):
    browser = webdriver.Chrome()
    browser.get(link2)

    input_first_name = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
    input_first_name.send_keys("AAA")

    input_last_name = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
    input_last_name.send_keys("AAA")

    input_email = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
    input_email.send_keys("AAA")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    self.assertEqual("Congratulations! You have successfully registered!", \
      welcome_text, "Should be same registration text")
    
if __name__ == "__main__":
  unittest.main()
