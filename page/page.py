from page.add_contact_page import AddContactPage
from page.contact_page import ContactPage
from page.message_list_page import MessageListPage
from page.new_message_page import NewMessagePage
from page.saved_contact_page import SavedContactPage


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def message_list(self):
        return MessageListPage(self.driver)

    @property
    def new_message(self):
        return NewMessagePage(self.driver)

    @property
    def add_contact(self):
        return AddContactPage(self.driver)

    @property
    def contact(self):
        return ContactPage(self.driver)

    @property
    def saved_contact(self):
        return SavedContactPage(self.driver)