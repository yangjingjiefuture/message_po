import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args",analyze_data("contact_data","test_add_phone"))
    def test_add_phone(self,args):
        name = args["name"]
        nickname = args["nickname"]
        phone = args["phone"]
        self.page.contact.click_add_contact()
        self.page.add_contact.input_name(name)
        self.page.add_contact.input_nickname(nickname)
        self.page.add_contact.input_phone(phone)
        # self.page.add_contact.press_back()
        # assert self.page.saved_contact.get_name_text_vie_text() == name

    @pytest.mark.parametrize("args", analyze_data("contact_data", "test_add_email"))
    def test_add_email(self,args):
        name = args["name"]
        email = args["email"]
        self.page.contact.click_add_contact()
        self.page.add_contact.input_name(name)
        self.page.add_contact.input_email(email)