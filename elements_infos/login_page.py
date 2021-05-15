import os
from selenium import webdriver
from selenium.webdriver.common.by import By
current = os.path.dirname(__file__)
driver_path = os.path.join(current, '../webdriver/chromedriver.exe')

"""页面作为类 控件作为属性 操作作为方法"""


class Login_Page:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.username_inputbox = self.driver.find_element(By.XPATH, '//input[@id="account"]')  # 属性 ==》页面上的控件
        self.password_inputbox = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        # self.keeplogin_checkbox = self.driver.find_element(By.XPATH, 'input[name="keepLogin[]"]')

    def input_username(self, username):  # 方法 ==》 空间的操作
        self.username_inputbox.send_keys(username)

    def input_password(self, password):
        self.password_inputbox.send_keys(password)

    def click_login(self):
        self.login_button.click()


if __name__ == '__main__':
    login_page = Login_Page()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
