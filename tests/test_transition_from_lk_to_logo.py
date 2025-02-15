from locators import ElementLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_transition_from_lk_to_constructor_successful(driver, authorization):
    lk_button = driver.find_element(*ElementLocators.LK_BUTTON)
    lk_button.click()

    logo = driver.find_element(*ElementLocators.STELLAR_BURGERS_LOGO)
    logo.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   (ElementLocators.CONSTRUCTOR_HEADER))
    constructor_header = driver.find_element(*ElementLocators.CONSTRUCTOR_HEADER)

    assert constructor_header.is_displayed()

    driver.quit()