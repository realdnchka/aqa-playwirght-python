from configuration import Configuration


class BasePage:
    def __init__(self, page):
        self.url = Configuration().url
