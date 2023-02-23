import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://facebook.com')

driver.implicitly_wait(1)
driver.find_element(By.NAME, 'email').send_keys('200103257@stu.sdu.edu.kz')
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'pass').send_keys('12345678')
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'login').click()
time.sleep(5)