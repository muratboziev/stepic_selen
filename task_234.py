from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".btn.btn-primary")
    btn1.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    #alert.send_keys(123)
    #confirm.dismiss()
    alert.accept()

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
