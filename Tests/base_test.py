from configuration import Configuration
from Helpers.logger import Logger
import pytest


class BaseTest:
    config = Configuration()
    log = Logger()
