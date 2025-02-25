from locators import ElementLocators

class TestConstructorTransitions:

    def test_transition_to_bun_successful(self, driver):
        sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
        sauce.click()
        bun = driver.find_element(*ElementLocators.BUN_BUTTON)
        bun.click()
        attribute_value = bun.get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in attribute_value

    def test_transition_to_filling_successful(self, driver):
        filling = driver.find_element(*ElementLocators.FILLING_BUTTON)
        filling.click()

        attribute_value = filling.get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in attribute_value

    def test_transition_to_sauce_successful(self, driver):
        sauce = driver.find_element(*ElementLocators.SAUCE_BUTTON)
        sauce.click()

        attribute_value = sauce.get_attribute('class')

        assert 'tab_tab_type_current__2BEPc' in attribute_value

