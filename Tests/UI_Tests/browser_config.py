import playwright.sync_api
import configuration


class BrowserConfig:
    def __init__(self):
        self.playwright = playwright.sync_api.sync_playwright().start()
        self.browser_name = configuration.Configuration().browser_name
        self.is_headless = configuration.Configuration().is_headless == 'true'
        self.browser = self.switch_browser()

    def switch_browser(self):
        match self.browser_name:
            case "chrome":
                return self.playwright.chromium.launch(channel=self.browser_name, headless=self.is_headless)
