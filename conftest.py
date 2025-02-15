import pytest
from selenium import webdriver
from locators import ElementLocators

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://stellarburgers.nomoreparties.site/')
    return chrome_driver

@pytest.fixture()
def email_password():
    return {'email': 'Andryuschenko15qa@gmail.com', 'password':'123456'}

@pytest.fixture()
def authorization(driver, email_password):
    lk_button = driver.find_element(*ElementLocators.LK_BUTTON)
    lk_button.click()

    login_email_input = driver.find_element(*ElementLocators.LOGIN_EMAIL)
    login_email_input.send_keys(email_password['email'])

    login_password_input = driver.find_element(*ElementLocators.LOGIN_PASSWORD)
    login_password_input.send_keys(email_password['password'])

    login_button = driver.find_element(*ElementLocators.LK_LOGIN_BUTTON)
    login_button.click()

    return authorization