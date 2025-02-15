from conftest import driver
from locators import ElementLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_transition_into_lk_successful(driver, authorization):
    lk_button = driver.find_element(*ElementLocators.LK_BUTTON)
    lk_button.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ElementLocators.EXIT_BUTTON))
    exit_button = driver.find_element(*ElementLocators.EXIT_BUTTON)

    assert exit_button.is_displayed()

    driver.quit()
