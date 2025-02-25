from locators import ElementLocators

class TestConstructorTransitions:

    def test_transition_to_bun_successful(self, driver):
        sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
        sauce.click()

        bun = driver.find_element(*ElementLocators.BUN_BUTTON)
        bun.click()

        assert bun.is_enabled()

    def test_transition_to_filling_successful(self, driver):
        filling_button = driver.find_element(*ElementLocators.FILLING_BUTTON)
        filling_button.click()

        assert filling_button.is_enabled()

    def test_transition_to_sauce_successful(self, driver):
        sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
        sauce.click()

        assert sauce.is_enabled()

