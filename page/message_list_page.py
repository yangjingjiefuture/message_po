from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessageListPage(BaseAction):
    # 添加短信
    add_message_button = By.ID, "com.android.mms:id/action_compose_new"

    def click_add_message(self):
        self.click(self.add_message_button)

