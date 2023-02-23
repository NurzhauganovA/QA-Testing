from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
link = 'https://hh.kz'


def getURLWebSite(url):
    driver.get(url)
    time.sleep(5)


getURLWebSite(link)


def test_example(base_url):
    base_url = link
    assert "errorPageContainer" in [elem.get_attribute("id") for elem in driver.find_elements_by_css_selector("body > div")]


driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a').click()
time.sleep(7)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[2]/span[2]/a').click()
time.sleep(7)

driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('200103257@stu.sdu.edu.kz', Keys.ENTER)
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('17672351', Keys.ENTER)
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/a[1]').click()
time.sleep(7)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[1]/div/div/div/div[5]/span/button').click()
time.sleep(20)

driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]').send_keys('Python Junior', Keys.ENTER)
time.sleep(20)

vacancy = driver.find_elements(By.CLASS_NAME, 'bloko-header-section-3')[0].text
time.sleep(10)

vacancy = vacancy.split(' ')

print(f'Number of available vacancies: {vacancy[0]}')
driver.close()