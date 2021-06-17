import os
from selenium import webdriver

cur_path = os.path.dirname(__file__)
default_path = os.path.join(cur_path, '..', '\webdriver\chromedriver.exe')


class Browser:
    def __init__(self, driver_name, driver_path=default_path):
        self.driver_path = driver_path
        self.driver_name = driver_name

    def get_browser_driver(self):
        if self.driver_name.lower == 'chrome':
            driver = webdriver.Chrome(executable_path=self.driver_path)
            return driver
        if self.driver_name.lower == 'firefox':
            driver = webdriver.Firefox()
        if self.driver_name.lower == 'IE':
            driver = webdriver.Ie()
            return driver


if __name__ == '__main__':
    Browser('chrome').get_browser_driver().get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
