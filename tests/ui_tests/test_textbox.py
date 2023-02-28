from helpers import form_generation as fg
from tests.ui_tests.base_test_ui import BaseTestUi
from page_objects import TextBoxPage


class TestTextBox(BaseTestUi):
    def test_textbox_compare_result(self):
        text_box_page = TextBoxPage(self.page)
        form = fg.generate_form()

        self.page.goto(text_box_page.url)
        text_box_page.fill_form_dto(form)
        text_box_page.submit_button_click()

        assert form.__eq__(text_box_page.get_form_dto())
