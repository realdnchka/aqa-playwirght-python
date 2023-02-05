from tests.api_tests.base_test_api import BaseTestApi
from helpers import user_generation as ug


class TestRegistration(BaseTestApi):
    def test_registration_api(self):
        user = ug.generate_user()
        self.api_helper.url = self.config.registration_url
        self.api_helper.data = {
            "email": user.email,
            "password": user.password,
            "repeat_password": user.password
        }

        response = self.api_helper.make_request(self.api_helper, method="post")

        self.log.logger.info(f'Asserting - {response} == 201')
        assert response == 201
