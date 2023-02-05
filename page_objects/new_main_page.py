from page_objects.new_base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: BasePage):
        super().__init__(page)
        self.btn_login = '//*[@id="usrbar"]/div[1]/div/div/div[1]'
        self.page = page

    def btn_login_click(self):
        self.page.click(self.btn_login)
