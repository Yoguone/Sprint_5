from locators import ElementLocators


def test_transition_to_bun_successful(driver):
    sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
    sauce.click()

    bun = driver.find_element(*ElementLocators.BUN_BUTTON)
    bun.click()

    assert bun.is_enabled()

    driver.quit()