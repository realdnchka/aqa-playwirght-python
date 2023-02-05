from Tests.base_test import BaseTest
from Helpers import api_helper as api
import pytest


class BaseTestApi(BaseTest):
    api_helper = api.ApiHelper

    def __int__(self):
        BaseTest.__init__(self)

    @pytest.fixture(autouse=True)
    def before_each_test_api(self):
        self.log.__int__("API")
        self.log.logger.info("Start test")
        yield
        self.log.logger.info("End test")