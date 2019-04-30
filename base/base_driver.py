from appium import webdriver


def init_driver():
        desired_caps = dict()
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app信息
        # 短信
        # desired_caps['appPackage'] = 'com.android.mms'
        # desired_caps['appActivity'] = '.ui.ConversationList'
        # 通讯录
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        # 不重置应用
        desired_caps['noReset'] = True

        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)