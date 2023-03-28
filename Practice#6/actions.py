import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://gate2home.com/English-Keyboard')
time.sleep(5)

word_id = [
    "kb_bcaps", "kb_b26", "kb_bcaps", "kb_b20", "kb_b18", "kb_b22", "kb_b43", "kb_b26", "kb_b18", "kb_b21", "kb_b22", "kb_b42",
    "kb_bspace", "kb_b21", "kb_b42", "kb_bspace", "kb_bcaps", "kb_b18", "kb_bcaps", "kb_b16", "kb_b27", "kb_b18", "kb_b21", "kb_b42", "kb_b30"
]

word_items = []

for word in range(len(word_id)):
    word_items.append(driver.find_element(By.XPATH, f'//div[@id="{word_id[word]}"]').click())
    driver.implicitly_wait(5)

actions = ActionChains(driver)

for word in range(len(word_items)):
    actions.click(word_items[word])
    driver.implicitly_wait(5)

driver.implicitly_wait(5)
text = driver.find_element(By.XPATH, '//div[@id="textbox1_freetext"]')
print(f'The result is: {text.text}')