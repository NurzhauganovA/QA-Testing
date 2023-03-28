import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get('https://www.calculator.net/')
driver.implicitly_wait(10)

first_number = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(2) > span:nth-child(3)")
second_number = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(2) > span:nth-child(1)")

equal = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(4)")

clear_output = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(3)")

addition = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(1) > span:nth-child(4)")

subtraction = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(2) > span:nth-child(4)")

multiplication = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(3) > span:nth-child(4)")

division = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(4) > span:nth-child(4)")

actions = ActionChains(driver)

actions.click(first_number)
actions.click(addition)
actions.click(second_number)
actions.click(equal)
actions.click(clear_output)

actions.click(first_number)
actions.click(subtraction)
actions.click(second_number)
actions.click(equal)
actions.click(clear_output)

actions.click(first_number)
actions.click(multiplication)
actions.click(second_number)
actions.click(equal)
actions.click(clear_output)

actions.click(first_number)
actions.click(division)
actions.click(second_number)
actions.click(equal)
actions.click(clear_output)
actions.perform()

results = driver.find_elements(By.ID, "scihistory")
for result in results:
    print(result.text)

time.sleep(5)