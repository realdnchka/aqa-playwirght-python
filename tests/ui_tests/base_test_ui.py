import pytest
from tests.base_test import BaseTest
from tests.ui_tests.browser_config import BrowserConfig


class BaseTestUi(BaseTest):
    browser = BrowserConfig().browser
    page = browser.new_page()

    @pytest.fixture(autouse=True)
    def before_each_test_ui(self):
        self.log.logger.info("Start test")
        yield
        self.log.logger.info("End test")
