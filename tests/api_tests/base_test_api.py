import pytest

from helpers.logger import Logger
from tests.base_test import BaseTest
from helpers import api_helper as api


class BaseTestApi(BaseTest):
    api_helper = api.ApiHelper
    log = BaseTest.log
    log.create_logger("API")
