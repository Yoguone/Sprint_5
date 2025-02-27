from conftest import generate_password
from locators import ElementLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistrationForm:

    def test_registration_successful(self,driver, generate_email, generate_password):
        main_login_button = driver.find_element(*ElementLocators.MAIN_PAGE_LOGIN_BUTTON)
        main_login_button.click()

        registration_link = driver.find_element(*ElementLocators.REGISTRATION_LINK)
        registration_link.click()

        registration_name_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_NAME_INPUT)
        registration_name_input.send_keys('Alexandr')

        registration_email_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_EMAIL_INPUT)
        registration_email_input.send_keys(generate_email)

        registration_password_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_PASSWORD_INPUT)
        registration_password_input.send_keys(generate_password)

        registration_button = driver.find_element(*ElementLocators.REGISTRATION_BUTTON)
        registration_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.ENTER_HEADER))

        enter_header = driver.find_element(*ElementLocators.ENTER_HEADER)

        assert enter_header.is_displayed()

    def test_invalid_password_is_displayed(self,driver, generate_email):
        main_login_button = driver.find_element(*ElementLocators.MAIN_PAGE_LOGIN_BUTTON)
        main_login_button.click()

        registration_link = driver.find_element(*ElementLocators.REGISTRATION_LINK)
        registration_link.click()

        registration_name_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_NAME_INPUT)
        registration_name_input.send_keys('Alexandr')

        registration_email_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_EMAIL_INPUT)
        registration_email_input.send_keys(generate_email)

        registration_password_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_PASSWORD_INPUT)
        registration_password_input.send_keys('123')

        registration_button = driver.find_element(*ElementLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ElementLocators.INVALID_PASSWORD))

        invalid_password = driver.find_element(*ElementLocators.INVALID_PASSWORD)
        assert invalid_password.is_displayed()