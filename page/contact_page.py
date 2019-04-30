from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class ContactPage(BaseAction):

    # 添加联系人
    add_contact_button = By.ID,"com.android.contacts:id/floating_action_button"
    @allure.step(title='通讯录 - 点击新建联系人')
    def click_add_contact(self):
        self.click(self.add_contact_button)