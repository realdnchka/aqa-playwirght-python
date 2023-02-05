from Tests.API_Tests.base_test_api import BaseTestApi
from Helpers import user_generation as ug


class TestRegistration(BaseTestApi):
    def __int__(self):
        BaseTestApi.__init__()

    def test_registration_api(self):
        user = ug.generate_user()
        self.api_helper.url = self.config.registration_url
        self.api_helper.data = {
            "email": user.email,
            "password": user.password,
            "repeat_password": user.password
        }

        response = self.api_helper.make_request(self.api_helper, method="post")
        assert response == 201
