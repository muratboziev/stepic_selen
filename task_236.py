from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    time.sleep(1)

    x = browser.find_element_by_id("input_value").text
    x = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(x)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
