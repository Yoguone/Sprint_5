from locators import ElementLocators

def test_transition_to_filling_successful(driver):
    filling_button = driver.find_element(*ElementLocators.FILLING_BUTTON)
    filling_button.click()

    assert filling_button.is_enabled()

    driver.quit()
