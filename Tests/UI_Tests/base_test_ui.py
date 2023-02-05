from Tests.base_test import BaseTest
from Tests.UI_Tests.browser_config import BrowserConfig
import pytest


class BaseTestUi(BaseTest):
    browser = BrowserConfig().browser
    page = browser.new_page()

    @pytest.fixture(autouse=True)
    def before_each_test_ui(self):
        self.log.__int__(name='UI')
        self.log.logger.info("Start test")
        yield
        self.log.logger.info("End test")