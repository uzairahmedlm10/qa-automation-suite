import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:

    def dropdown(self, locator, value):
        dropdown = Select(locator)
        dropdown.select_by_value(value)

    def window_tabs(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def waitOnVisibility(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((locator)))
