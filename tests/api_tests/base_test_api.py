import pytest

from helpers.logger import Logger
from tests.base_test import BaseTest
from helpers import api_helper as api


class BaseTestApi(BaseTest):
    api_helper = api.ApiHelper
    log = Logger("API")

    @pytest.fixture(autouse=True)
    def before_each_test_api(self):
        self.log.logger.info("Start test")
        yield
        self.log.logger.info("End test")
