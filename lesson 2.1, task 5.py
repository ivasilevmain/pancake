from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    button = browser.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
   
   
   
