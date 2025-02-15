from locators import ElementLocators


def test_transition_to_sauce_successful(driver):
    sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
    sauce.click()

    assert sauce.is_enabled()

    driver.quit()