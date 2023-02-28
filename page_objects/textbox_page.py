from page_objects.base_page import BasePage
from helpers.form_dto import Form
from configuration import Configuration


class TextBoxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = self.url + 'text-box'

        # elements
        self.name_input = "//*[@id='userName']"
        self.email_input = "//*[@id='userEmail']"
        self.current_address_input = "(//*[@id='currentAddress'])[1]"
        self.permanent_address_input = "(//*[@id='permanentAddress'])[1]"
        self.submit_button = "//*[@id='submit']"
        self.result_name = "//*[@id='name']"
        self.result_email = "//*[@id='email']"
        self.result_current_address = "(//*[@id='currentAddress'])[2]"
        self.result_permanent_address = "(//*[@id='permanentAddress'])[2]"

    def submit_button_click(self):
        self.click(self.submit_button)

    def name_input_send_keys(self, text):
        self.send_keys(self.name_input, text)

    def email_input_send_keys(self, text):
        self.send_keys(self.email_input, text)

    def current_address_send_keys(self, text):
        self.send_keys(self.current_address_input, text)

    def permanent_address_send_keys(self, text):
        self.send_keys(self.permanent_address_input, text)

    def result_name_get_text(self):
        return self.get_text(self.result_name)

    def result_email_get_text(self):
        return self.get_text(self.result_email)

    def result_current_address_get_text(self):
        return self.get_text(self.result_current_address)

    def result_permanent_address_get_text(self):
        return self.get_text(self.result_permanent_address)

    def fill_form_dto(self, form):
        self.name_input_send_keys(form.name)
        self.email_input_send_keys(form.email)
        self.current_address_send_keys(form.current_address)
        self.permanent_address_send_keys(form.permanent_address)

    def get_form_dto(self):
        name = self.result_name_get_text().split(':')[1]
        email = self.result_email_get_text().split(':')[1]
        current_address = self.result_current_address_get_text().split(':')[1]
        permanent_address = self.result_permanent_address_get_text().split(':')[1]

        return Form(name, email, current_address, permanent_address)
