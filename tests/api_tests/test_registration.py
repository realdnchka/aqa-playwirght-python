from helpers.api_helper.request_builder import RequestBuilder
from tests.api_tests.base_test_api import BaseTestApi
from helpers import user_generation as ug


class TestRegistration(BaseTestApi):
    def test_registration_api(self):
        user = ug.generate_user()
        url = self.config.registration_url
        data = {
            "email": user.email,
            "password": user.password,
            "repeat_password": user.password
        }

        request = RequestBuilder().with_data(data).with_url(url).with_method("post").get_request()

        response = self.api_helper.make_request(request)

        self.log.logger.info(f'Asserting - {response} == 201')
        assert response == 201
