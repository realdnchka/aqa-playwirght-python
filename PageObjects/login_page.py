import PageObjects


class LoginPage(PageObjects.AbstractPage):
    def __init__(self, page):
        #elements
        super(LoginPage, self).__init__(page)
        self.title = page.locator("//div[@class='auth-form__body']//div[contains(text(), 'Вход')]")
        self.login_btn = page.locator("")
        self.login_input = page.locator("")
        self.password_input = page.locator("")
        self.register_btn = page.locator("//a[contains(@href, '/registration')]")

    def login_btn_click(self):
        self.login_btn.click()

    def login_text_fill(self, text):
        self.login_input.fill(text)

    def password_text_fill(self, text):
        self.password_input.fill(text)

    def register_btn_click(self):
        self.register_btn.click()

    def title_get(self):
        return self.title
