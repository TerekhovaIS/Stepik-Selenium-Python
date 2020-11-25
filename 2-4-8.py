from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_css_selector('[id="book"]')
button.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    option = browser.find_element_by_css_selector("input[id='answer']")
    option.send_keys(y)

    button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()