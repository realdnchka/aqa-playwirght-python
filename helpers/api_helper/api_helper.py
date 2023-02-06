import requests

from helpers.api_helper.request import Request
from helpers.logger import Logger


class ApiHelper:
    log = Logger()
    log.create_logger("API")

    def make_request(self, request: Request):
        resp = None

        self.log.logger.info(f"Make request '{request.method}' to {request.url} with data: "
                             f"\n {request.data}")
        if request.method == "post":
            resp = requests.post(request.url, json=request.data)
        if request.method == "get":
            resp = requests.get(request.url)

        self.log.logger.info(f"Response: {resp.status_code}")
        return resp.status_code
