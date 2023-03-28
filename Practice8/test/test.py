from selenium import webdriver
from Practice8.authorization.authorization import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("username")
    login_page.enter_password("password")
    login_page.click_login_button()
    assert driver.current_url != "http://www.google.com/"
    driver.quit()
