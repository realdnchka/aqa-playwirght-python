from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        #elements
        super().__init__(page)
        self.title = page.locator("//div[@class='auth-form__body']//div[contains(text(), 'Вход')]")
        self.login_btn = ""
        self.login_input = ""
        self.password_input = ""
        self.register_btn = "//a[contains(@href, '/registration')]"

    def login_btn_click(self):
        self.click(self.login_btn)

    def login_text_fill(self, text):
        self.send_keys(self.login_input, text)

    def password_text_fill(self, text):
        self.send_keys(self.password_input, text)

    def register_btn_click(self):
        self.click(self.register_btn)

    def title_get(self):
        return self.title
