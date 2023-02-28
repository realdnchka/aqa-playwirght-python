import json


class Configuration:
    def __init__(self):
        configuration_file = open('config.json')
        configuration = json.load(configuration_file)
        self.browser_name = configuration["browser"]
        self.is_headless = configuration["headless"]
        self.url = configuration["urls"]["url"]
        self.logging = configuration["logging"]
        self.timeout = int(configuration["timeout"])
        # TODO add timeout config
