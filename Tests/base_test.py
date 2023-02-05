from configuration import Configuration
from Helpers.logger import Logger
import pytest


class BaseTest:
    config = Configuration()
    if config.logging == 'true':
        log = Logger()
