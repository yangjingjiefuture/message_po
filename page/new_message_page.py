from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):
    # 接收者
    phone_recipients_editor = By.ID, "com.android.mms:id/recipients_editor"

    # 短信文本框
    message_edit_text = By.ID, "com.android.mms:id/embedded_text_editor"

    # 发送短信
    send_button =  By.ID, "com.android.mms:id/send_button_sms"

    def input_phone(self,content):
        self.input(self.phone_recipients_editor,content)

    def input_message(self,content):
        self.input(self.message_edit_text,content)

    def click_send_message(self):
        self.click(self.send_button)