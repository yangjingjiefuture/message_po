from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):

    # 保存后的联系人
    name_text_view = By.ID,"com.android.contacts:id/large_title"

    def get_name_text_vie_text(self):
        return self.find_element(self.name_text_view).text