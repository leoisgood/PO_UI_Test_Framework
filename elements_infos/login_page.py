import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
"""页面作为类 控件作为属性 操作作为方法"""


class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name': '用户名输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="account"]',
        #                           'time_out': 5}
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'time_out': 5}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'time_out': 5}
        elements = ElementDataUtils().get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    def input_username(self, username):  # 方法 ==》 控件的操作
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)
        logger.info('登录按钮是%s' % self.login_button)


if __name__ == '__main__':
    current = os.path.dirname(__file__)
    driver_path = os.path.join(current, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = Login_Page(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.wait(3)
    login_page.close_browser()

