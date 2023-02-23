import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get('https://the-internet.herokuapp.com/dynamic_controls')

driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button').click()
driver.implicitly_wait(10)
message = driver.find_element(By.ID, 'message')
if message.text == "It's gone!":
    driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button').click()
driver.implicitly_wait(10)
message = driver.find_element(By.ID, 'message')
if message.text == "It's back!":
    print(message.text)
    driver.close()