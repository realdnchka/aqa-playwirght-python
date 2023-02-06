from tests.base_test import BaseTest
from helpers import ApiHelper


class BaseTestApi(BaseTest):
    api_helper = ApiHelper()
    log = BaseTest.log
    log.create_logger("API")
