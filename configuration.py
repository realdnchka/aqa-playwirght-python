import json
import playwright.sync_api


class Configuration:
    configuration_file = open("config.json")
    configuration = json.load(configuration_file)
    browser_name = configuration["browser"]
    is_headless = configuration["headless"] == 'True'
    url = configuration["url"]

    def __init__(self):
        self.playwright = playwright.sync_api.sync_playwright().start()
        self.browser = self.switch_browser()

    def switch_browser(self):
        match self.browser_name:
            case "chrome":
                return self.playwright.chromium.launch(channel=self.browser_name, headless=self.is_headless)
