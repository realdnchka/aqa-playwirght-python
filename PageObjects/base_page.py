import sys

import playwright
from playwright.sync_api import expect

from configuration import Configuration
from Helpers.logger import Logger


class BasePage:
    # TODO make another implementation of base page: inheriting of playwright.Page
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
            sys.exit()

    def send_keys(self, locator: str, text: str):
        try:
            self.log.logger.info('Fill in ' + locator)
            self.page.locator(locator).fill(text)
        except playwright.sync_api.Error as e:
            self.log.logger.error('Unable to fill ' + locator + '\n{}'.format(e))
            sys.exit()

    def is_visible(self, locator: str):
        try:
            self.log.logger.info('Visibility check of' + locator)
            expect(self.page.locator(locator)).to_be_visible()

        except playwright.sync_api.Error as e:
            self.log.logger.error(locator + '\n{}'.format(e))
            sys.exit()
    # TODO add decorators for other actions
