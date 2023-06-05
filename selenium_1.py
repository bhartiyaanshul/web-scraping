
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome() 
driver.get("https://www.amazon.in/")

search = driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("iphone")
search.send_keys(Keys.RETURN)

# # WebDriverWait(driver, timeout=10).until(
# # el = driver.find_element(By.ID, "cm_cr-review_list"))
# main = driver.find_element(By.CLASS_NAME,'cz bm da db dc dd')
# for n in main:
#     print(n)

# driver.quit()


time.sleep(5)
driver.quit()
