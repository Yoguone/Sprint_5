from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ElementLocators

def test_invalid_password_is_displayed(driver):
    main_login_button = driver.find_element(*ElementLocators.MAIN_PAGE_LOGIN_BUTTON)
    main_login_button.click()

    registration_link = driver.find_element(*ElementLocators.REGISTRATION_LINK)
    registration_link.click()

    registration_name_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_NAME_INPUT)
    registration_name_input.send_keys('Alexandros')

    registration_email_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_EMAIL_INPUT)
    registration_email_input.send_keys('Andryuschenko15qa@gmail.com')

    registration_password_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_PASSWORD_INPUT)
    registration_password_input.send_keys('123')

    registration_button = driver.find_element(*ElementLocators.REGISTRATION_BUTTON)
    registration_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.INVALID_PASSWORD))

    invalid_password = driver.find_element(*ElementLocators.INVALID_PASSWORD)
    assert invalid_password.is_displayed()

    driver.quit()
