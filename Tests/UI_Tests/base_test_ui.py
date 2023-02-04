from Tests.base_test import BaseTest
from Tests.UI_Tests.browser_config import BrowserConfig


class BaseTestUi(BaseTest):
    browser = BrowserConfig().browser
