from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    option = browser.find_element_by_css_selector("input[id='answer']")
    option.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()