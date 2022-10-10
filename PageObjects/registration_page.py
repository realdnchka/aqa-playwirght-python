import PageObjects


class RegistrationPage(PageObjects.AbstractPage):
    def __init__(self, page):
        #elements
        super(RegistrationPage, self).__init__(page)
        self.url = self.url[0: 8] + 'profile' + self.url[11: -1] + '/registration'
        self.email_input = page.locator("//input[@type='email']")
        self.password_input = page.locator("(//input[@type='password'])[1]")
        self.password_repeat_input = page.locator("(//input[@type='password'])[2]")
        self.accept_checkbox = page.locator("//span[@class='i-checkbox__faux']")
        self.registration_btn = page.locator("//button[@type='submit']")
        self.email_confirm_input = page.locator("//nobr[contains(text(), 'e-mail')]")
        self.success_registration_text = page.locator("//nobr[contains(text(), 'e-mail')]")

    def email_input_fill(self, text: str):
        self.email_input.fill(text)

    def password_input_fill(self, text: str):
        self.password_input.fill(text)

    def password_repeat_input_fill(self, text: str):
        self.password_repeat_input.fill(text)

    def accept_checbox_click(self):
        self.accept_checkbox.click()

    def registration_btn_click(self):
        self.registration_btn.click()
