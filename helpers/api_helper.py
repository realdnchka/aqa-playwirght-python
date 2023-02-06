import requests

from helpers.logger import Logger


class ApiHelper:
    log = Logger()
    log.create_logger("API")

    def __init__(self):
        self.url = ""
        self.data = {}

    def make_request(self, method):
        resp = None

        self.log.logger.info(f"Make request '{method}' to {self.url} with data: "
                             f"\n {self.data}")
        if method == "post":
            resp = requests.post(self.url, json=self.data)
        if method == "get":
            resp = requests.get(self.url)

        self.log.logger.info(f"Response: {resp.status_code}")
        return resp.status_code
