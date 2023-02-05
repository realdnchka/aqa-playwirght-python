from PageObjects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        #elements
        super(MainPage, self).__init__(page)
        self.login_btn = '//*[@id="userbar"]/div[1]/div/div/div[1]'

    def login_btn_click(self):
        self.click(self.login_btn)
