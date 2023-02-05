from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page):
        # elements
        super().__init__(page)
        self.url = self.url[0: 8] + 'profile' + self.url[11: -1] + '/registration'
        self.email_input = "//input[@type='email']"
        self.password_input = "(//input[@type='password'])[1]"
        self.password_repeat_input = "(//input[@type='password'])[2]"
        self.accept_checkbox = "//span[@class='i-checkbox__faux']"
        self.registration_btn = "//button[@type='submit']"
        self.email_confirm_input = "//nobr[contains(text(), 'e-mail')]"
        self.success_registration_text = "//nobr[contains(text(), 'e-mail')]"

    def email_input_fill(self, text: str):
        self.send_keys(self.email_input, text)

    def password_input_fill(self, text: str):
        self.send_keys(self.password_input, text)

    def password_repeat_input_fill(self, text: str):
        self.send_keys(self.password_repeat_input, text)

    def accept_checkbox_click(self):
        self.click(self.accept_checkbox)

    def registration_btn_click(self):
        self.click(self.registration_btn)

    def success_registration_text_is_visible(self):
        self.is_visible(self.success_registration_text)
