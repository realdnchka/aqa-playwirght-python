from playwright.sync_api import expect
from Helpers import user_generation as ug
from Tests.UI_Tests.base_test_ui import BaseTestUi
from PageObjects import MainPage, LoginPage, RegistrationPage


class TestRegistration(BaseTestUi):
    def test_registration_ui(self):
        main_page = MainPage(self.page)
        login_page = LoginPage(self.page)
        registration_page = RegistrationPage(self.page)
        user = ug.generate_user()

        self.page.goto(main_page.url)
        main_page.login_btn_click()
        expect(login_page.title_get()).to_be_visible()

        login_page.register_btn_click()
        expect(self.page).to_have_url(registration_page.url)

        registration_page.email_input_fill(user.email)
        registration_page.password_input_fill(user.password)
        registration_page.password_repeat_input_fill(user.password)
        registration_page.accept_checkbox_click()
        registration_page.registration_btn_click()

        registration_page.success_registration_text_is_visible()
