import json
import playwright.sync_api


class Configuration:
    def __init__(self):
        configuration_file = open('config.json')
        configuration = json.load(configuration_file)
        self.browser_name = configuration["browser"]
        self.is_headless = configuration["headless"]
        self.url = configuration["urls"]["url"]
        self.registration_url = configuration["urls"]["registration_url"]
        # self.playwright = playwright.sync_api.sync_playwright().start()
    #     self.browser = self.switch_browser()
    #
    # def switch_browser(self):
    #     match self.browser_name:
    #         case "chrome":
    #             return self.playwright.chromium.launch(channel=self.browser_name, headless=self.is_headless)
