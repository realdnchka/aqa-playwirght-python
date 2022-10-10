from playwright.sync_api import expect
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
# from PageObjects import MainPage, LoginPage, RegistrationPage
from Helpers import user_generation as ug
from Helpers import api_helper as api
from configuration import Configuration

browser = Configuration().browser


# def test_registration_ui():
#     page = browser.new_page()
#
#     main_page = MainPage(page)
#     login_page = LoginPage(page)
#     registration_page = RegistrationPage(page)
#     user = ug.generate_user()
#
#     page.goto(main_page.url)
#     main_page.login_btn_click()
#     expect(login_page.title_get()).to_be_visible()
#
#     login_page.register_btn_click()
#     expect(page).to_have_url(registration_page.url)
#
#     registration_page.email_input_fill(user.email)
#     registration_page.password_input_fill(user.password)
#     registration_page.password_repeat_input_fill(user.password)
#     registration_page.accept_checbox_click()
#     registration_page.registration_btn_click()
#
#     expect(registration_page.success_registration_text).to_be_visible()


def test_registration_api():
    api_helper = api.ApiHelper
    user = ug.generate_user()

    api_helper.url = "https://profile.onliner.by/sdapi/user.api/registration"
    api_helper.data = {
        "email": user.email,
        "password": user.password,
        "repeat_password": user.password
    }

    response = api_helper.make_request(api.ApiHelper, method="post")
    assert response == 201
