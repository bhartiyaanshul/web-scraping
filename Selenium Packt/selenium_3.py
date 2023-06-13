# This Program is for Browser Automation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# using chrome as a web browser
browser = webdriver.Chrome()

# declare the website to be automated
browser.get('http://techstepacademy.com/training-ground')

# finding element by css selector
element = browser.find_element(By.CSS_SELECTOR,'input[id="ipt1"]')

# key is sended to the element of the webpage
element.send_keys('Anshul')

# finding the element of the button
button = browser.find_element(By.XPATH,'//button[@id="b1"]')

# click functon is used for clicking the button
button.click()


time.sleep(5)
browser.quit()