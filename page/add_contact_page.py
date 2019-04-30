from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class AddContactPage(BaseAction):
    # 姓名
    name_textbox = By.XPATH, "//*[contains(@text,'姓名')]"
    # 昵称
    nickname_textbox = By.XPATH, "//*[contains(@text,'昵称')]"
    # 电话
    phone_textbox = By.XPATH, "//*[contains(@text,'电话')]"
    # 电子邮件
    email_textbox = By.XPATH, "//*[contains(@text,'电子邮件')]"

    @allure.step(title='新建联系人 - 输入姓名')
    def input_name(self,content):
        self.input(self.name_textbox,content)

    @allure.step(title='新建联系人 - 输入昵称')
    def input_nickname(self,content):
        self.input(self.nickname_textbox,content)

    @allure.step(title='新建联系人 - 输入手机号')
    def input_phone(self,content):
        self.input(self.phone_textbox,content)

    @allure.step(title='新建联系人 - 输入邮件')
    def input_email(self,content):
        self.input(self.email_textbox,content)