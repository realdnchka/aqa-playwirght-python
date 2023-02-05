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
                return \
                    self.playwright.chromium.launch(channel=self.browser_name, headless=self.is_headless)
            case "webkit":
                return \
                    self.playwright.webkit.launch(channel=self.browser_name, headless=self.is_headless)
            case "firefox":
                return \
                    self.playwright.firefox.launch(channel=self.browser_name, headless=self.is_headless)
            case "msedge":
                return \
                    self.playwright.chromium.launch(channel=self.browser_name, headless=self.is_headless)
            case _:
                raise Exception\
                    ('Browser name is not defined correctly. Check available names in README.md file')
