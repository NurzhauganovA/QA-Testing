import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://google.com')
driver.implicitly_wait(1)

driver.find_element(By.NAME, 'q').send_keys('Selenium', Keys.RETURN)
driver.implicitly_wait(3)

driver.find_element(By.XPATH, '//a[@href="https://www.selenium.dev/"]').click()