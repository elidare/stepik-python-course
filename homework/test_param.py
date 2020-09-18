import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def get_time():
    return str(math.log(int(time.time())))

exercises = [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
]

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('exercise', exercises)
def test_should_find_the_correct_text(browser, exercise):
    # open the page
    link = f"https://stepik.org/lesson/{exercise}/step/1"
    browser.get(link)

    # ввести правильный ответ
    # [data-type="string-quiz"] textarea
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-type='string-quiz'] textarea"))
    )

    answer = get_time()
    textarea.send_keys(answer)

    # нажать кнопку "Отправить"
    browser.find_element_by_class_name("submit-submission").click()

    # дождаться фидбека о том, что ответ правильный
    # class="attempt-message_correct"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "attempt-message_correct"))
    )

    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    correct_text = browser.find_element_by_class_name("smart-hints__hint").text
    assert "Correct!" == correct_text, "Correct text is not correct"
