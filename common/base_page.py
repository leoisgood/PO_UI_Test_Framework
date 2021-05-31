import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log_utils import logger


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装 -- > 二次封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址:%s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是：%s' % value)
        return value

    def close_browser(self):
        self.driver.close()
        logger.info('关闭浏览器')

    # 元素操作封装
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['time_out']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver, int(locator_timeout)) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))  # 显示等待
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        return element

    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素点击成功' % element_info['element_name'])

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容[%s]' % (element_info['element_name'], content))

    # 等待操作封装
    def wait(self, seconds):
        time.sleep(seconds)
        logger.info('等待[%s]秒' % seconds)
