import sys

import playwright
from playwright.sync_api import expect

from configuration import Configuration
from helpers.logger import Logger


class BasePage:
    # TODO make another implementation of base page: inheriting of playwright.Page
    log = Logger()
    log.create_logger("UI")

    def __init__(self, page: playwright.sync_api.Page):
        self.url = Configuration().url
        self.page = page

    def click(self, locator: str):
        try:
            self.log.logger.info(f'Click by {locator}')
            self.page.locator(locator).click()
        except playwright.sync_api.Error as e:
            self.log.logger.error(f'Unable to click by {locator} \n %s' % e)
            sys.exit()

    def send_keys(self, locator: str, text: str):
        try:
            self.log.logger.info(f'Fill in {locator}')
            self.page.locator(locator).fill(text)
        except playwright.sync_api.Error as e:
            self.log.logger.error(f'Unable to fill {locator}  \n %s' % e)
            sys.exit()

    def is_visible(self, locator: str):
        try:
            self.log.logger.info(f'Visibility check of {locator}')
            expect(self.page.locator(locator)).to_be_visible()

        except playwright.sync_api.Error as e:
            self.log.logger.error(f'{locator} + \n %s' % e)
            sys.exit()

    def get_text(self, locator: str):
        try:
            self.log.logger.info(f'Trying to get text of {locator}')
            return self.page.locator(locator).inner_text()
        except playwright.sync_api.Error as e:
            self.log.logger.error(f'{locator} + \n %s' % e)
            sys.exit()

    # TODO add decorators for other actions
