from PageObjects.abstract_page import AbstractPage


class MainPage(AbstractPage):
    def __init__(self, page):
        #elements
        super(MainPage, self).__init__(page)
        self.login_btn = page.locator('//*[@id="userbar"]/div[1]/div/div/div[1]')

    def login_btn_click(self):
        self.login_btn.click()
