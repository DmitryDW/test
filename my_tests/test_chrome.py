from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/webhp")
    elements = browser.find_elements(By.CSS_SELECTOR, ("textarea[class='gLFyf']"))
    for element in elements:
        element.send_keys('скачать yappy')

    button = browser.find_element(By.CSS_SELECTOR, "input.gNO89b")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

