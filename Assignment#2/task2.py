from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://drive.google.com/drive/my-drive")

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("200103257@stu.sdu.edu.kz")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
time.sleep(5)

driver.find_element(By.XPATH, "//input[@type='password']").send_keys("17672351")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
time.sleep(5)

test1_folder = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[2]/div/div/div/div')
test2_folder = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[3]/div/div/div/div')

actions = ActionChains(driver)
actions.drag_and_drop(test1_folder, test2_folder).perform()
time.sleep(3)

actions.double_click(test2_folder).perform()
time.sleep(7)

driver.find_element(By.CSS_SELECTOR, '#nt\:Dr > div.a-U-J.a-U-xc-J > div.a-U-Ze-j.a-U-ye-jm > div > div.c-Po.a-U-Ze-c-Vf > svg').click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '#nt\:Dr\;1 > div.a-U-J > div.a-U-Ze-j.a-U-ye-jm > div > div.c-Po.a-U-Ze-c-Vf > svg').click()
time.sleep(5)
return_folder = driver.find_element(By.XPATH, '//*[@data-tooltip = "test 1"]')
time.sleep(5)
my_drive = driver.find_element(By.XPATH, '//*[@id="nt:Dr"]/div[1]')

action = ActionChains(driver)
action.drag_and_drop(return_folder, my_drive).perform()
time.sleep(5)
action.double_click(my_drive).perform()
time.sleep(5)
driver.quit()