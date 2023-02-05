import sys
from typing import Literal
import typing
from playwright.sync_api import Page, Position, Error

from configuration import Configuration
from helpers.logger import Logger


class BasePage(Page):
    def __init__(self, page):
        super().__init__(page)
        self.log = Logger.get_instance()
        self.config = Configuration()
        self.page_url = self.config.url

    def click(
        self,
        selector: str,
        *,
        modifiers: typing.Optional[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Optional[Position] = None,
        delay: typing.Optional[float] = None,
        button: typing.Optional[Literal["left", "middle", "right"]] = None,
        click_count: typing.Optional[int] = None,
        timeout: typing.Optional[float] = None,
        force: typing.Optional[bool] = None,
        no_wait_after: typing.Optional[bool] = None,
        trial: typing.Optional[bool] = None,
        strict: typing.Optional[bool] = None
    ) -> None:
        try:
            self.log.logger.info(f'Click by {selector}')
            super().click(selector, modifiers=modifiers, position=position, delay=delay, button=button,
                          click_count=click_count, timeout=timeout, force=force, no_wait_after=no_wait_after, trial=trial,
                          strict=strict)
        except Error as e:
            self.log.logger.error(f'Unable to click by {selector} \n %s' % e)
            sys.exit()
