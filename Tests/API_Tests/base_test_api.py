from Tests.base_test import BaseTest
from Helpers import api_helper as api


class BaseTestApi(BaseTest):
    api_helper = api.ApiHelper

    def __int__(self):
        BaseTest.__init__(self)
