from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver =  webdriver.Chrome()
driver.get("https://www.amazon.in/")

link = driver.find_element(By.ID,"twotabsearchtextbox")
link.send_keys("iphone 14")
link.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.LINK_TEXT,"Apple iPhone 14 (128 GB) - Blue")
    )
    element.click()
except:
    driver.quit()


# time.sleep(5)
# driver.quit()

