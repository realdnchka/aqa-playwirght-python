from configuration import Configuration


class AbstractPage:
    def __init__(self, page):
        self.url = Configuration.url
