from locators import ElementLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_registration_successful(driver):
        main_login_button = driver.find_element(*ElementLocators.MAIN_PAGE_LOGIN_BUTTON)
        main_login_button.click()

        registration_link = driver.find_element(*ElementLocators.REGISTRATION_LINK)
        registration_link.click()

        registration_name_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_NAME_INPUT)
        registration_name_input.send_keys('Alexandros')

        registration_email_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_EMAIL_INPUT)
        registration_email_input.send_keys('Andryuschenko15qa@gmail.com')

        registration_password_input = driver.find_element(*ElementLocators.REGISTRATION_FORM_PASSWORD_INPUT)
        registration_password_input.send_keys('123456')

        registration_button = driver.find_element(*ElementLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.LK_LOGIN_BUTTON))

        login_email_input = driver.find_element(*ElementLocators.LOGIN_EMAIL)
        login_email_input.send_keys('Andryuschenko15qa@gmail.com')

        login_password_input = driver.find_element(*ElementLocators.LOGIN_PASSWORD)
        login_password_input.send_keys('123456')

        login_button = driver.find_element(*ElementLocators.LK_LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.OFFER_BUTTON))
        offer_button = driver.find_element(*ElementLocators.OFFER_BUTTON)
        assert offer_button.is_displayed()

        driver.quit()