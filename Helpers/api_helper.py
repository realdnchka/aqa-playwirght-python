import requests


class ApiHelper:
    def __init__(self):
        self.url = ""
        self.data = {}

    def make_request(self, method):
        resp = None

        if method == "post":
            resp = requests.post(self.url, json=self.data)
        if method == "get":
            resp = requests.get(self.url)

        return resp.status_code
