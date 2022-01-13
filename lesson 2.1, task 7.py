from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure_chest = browser.find_element_by_css_selector("[src='images/chest.png']")
    valuex = treasure_chest.get_attribute("valuex")
    x = valuex
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[id='robotsRule']")
    option1.click()
    button = browser.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
   
   
