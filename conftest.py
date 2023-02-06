import pytest

from helpers.logger import Logger


log = Logger()


@pytest.fixture(scope="session", autouse=True)
def before_after_tests():
    log.clear_logs()
    yield
    log.copy_last_logs()


@pytest.fixture(scope="function", autouse=True)
def before_after_each_test():
    log.create_logger("Base")
    log.logger.info("Start test")
    yield
    log.logger.info("End test")
