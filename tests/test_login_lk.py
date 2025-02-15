from locators import ElementLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_login_from_lk_successful(driver, email_password):
    lk_button = driver.find_element(*ElementLocators.LK_BUTTON)
    lk_button.click()

    login_email_input = driver.find_element(*ElementLocators.LOGIN_EMAIL)
    login_email_input.send_keys(email_password['email'])

    login_password_input = driver.find_element(*ElementLocators.LOGIN_PASSWORD)
    login_password_input.send_keys(email_password['password'])

    login_button = driver.find_element(*ElementLocators.LK_LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.OFFER_BUTTON))
    offer_button = driver.find_element(*ElementLocators.OFFER_BUTTON)
    assert offer_button.is_displayed()

    driver.quit()