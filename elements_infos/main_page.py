import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import Login_Page
from common.log_utils import logger

current = os.path.dirname(__file__)
driver_path = os.path.join(current, '../webdriver/chromedriver.exe')

"""页面作为类 控件作为属性 操作作为方法"""


class Main_Page:
    def __init__(self):
        """ 登陆成功之后才能识别元素"""
        self.logger = logger
        login_page = Login_Page()
        login_page.input_username('test01')
        login_page.input_password('newdream123')
        login_page.click_login()
        self.driver = login_page.driver # 把loginpage的driver赋值到当前driver
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.companyname_showbox = self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH, '//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')

    def get_companyname(self):  # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value

    def goto_myzone(self):  # 进入我的地盘菜单
        self.myzone_menu.click()

    def goto_product(self):  # 进入产品菜单
        self.product_menu.click()

    def get_username(self):  # 获取用户名
        value = self.username_showspan.text
        logger.info('获取用户名：' + str(value))
        return value


if __name__ == '__main__':
    main_page = Main_Page()
    main_page.goto_myzone()
    main_page.goto_product()
    username = main_page.get_username()
    print(username)
