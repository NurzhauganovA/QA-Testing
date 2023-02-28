import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Alerts.html')
time.sleep(5)

click_buttons = [
    "#OKTab > button",
    "body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(2) > a",
    "#CancelTab > button",
    "body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(3) > a",
    "#Textbox > button"
]

item_buttons = []

for button in range(len(click_buttons)):
    item_buttons.append(driver.find_element(By.CSS_SELECTOR, f'{click_buttons[button]}'))
    driver.implicitly_wait(2)
print(click_buttons)

for button in range(len(item_buttons)):
    item_buttons[button].click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(5)