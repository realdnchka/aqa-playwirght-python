import pytest
from tests.base_test import BaseTest
from helpers import api_helper as api


class BaseTestApi(BaseTest):
    api_helper = api.ApiHelper

    def __int__(self):
        BaseTest.__init__(self)

    @pytest.fixture(autouse=True)
    def before_each_test_api(self):
        self.log.get_instance()
        self.log.logger.info("Start test")
        yield
        self.log.logger.info("End test")
