from helpers.logger import Logger
from tests.base_test import BaseTest
from tests.ui_tests.browser_config import BrowserConfig


class BaseTestUi(BaseTest):
    browser = BrowserConfig().browser
    page = browser.new_page()
    page.set_default_timeout(BaseTest().config.timeout)
    log = BaseTest.log
    log.create_logger("UI")
