from helpers.api_helper.request import Request


class RequestBuilder:
    def __init__(self):
        self.request = Request()

    def with_method(self, method: str):
        self.request.method = method
        return self

    def with_data(self, data: dict):
        self.request.data = data
        return self

    def with_url(self, url: str):
        self.request.url = url
        return self

    def get_request(self):
        return self.request
