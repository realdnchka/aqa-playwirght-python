import traceback

import playwright.sync_api

from configuration import Configuration
from Helpers.logger import Logger


class BasePage:
    def __init__(self, page: playwright.sync_api.Page):
        self.url = Configuration().url
        self.page = page
        self.log = Logger.get_instance()

    def click(self, locator: str):
        try:
            self.log.logger.info('Click by ' + locator)
            self.page.locator(locator).click()
        except playwright.sync_api.Error as e:
            self.log.logger.error('Unable to click by ' + locator + '\n{}'.format(e))

