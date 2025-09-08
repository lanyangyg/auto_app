from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging


class BasePage:
    def __init__(self, appium_driver, timeout=5):
        """
        初始化方法
        :param driver: appium_driver实例
        :param timeout: 默认等待超时时间(秒)
        """
        self.driver = appium_driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)


    def find_element(self, locator, timeout=None):
        """
        查找单个元素
        """
        wait_time = timeout if timeout is not None else self.timeout
        by, value = locator
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            self.logger.error(f"find element fail (timeout {wait_time}s): {locator}")
            raise NoSuchElementException(f"find element fail: {locator}")


    def find_elements(self, locator, timeout=None):
        """
        查找多个元素，返回一个元素列表。
        """
        wait_time = timeout if timeout is not None else self.timeout
        by, value = locator
        try:
            elements = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((by, value))
            )
            self.logger.info(f"find {len(elements)} elements: {locator}")
            return elements
        except TimeoutException:
            self.logger.warning(f"can not find element: {locator} in {wait_time}s ")
            return [] # 在超时的情况下，返回一个空列表


    def click(self, locator, timeout=None):
        """
        点击元素
        """
        element = self.find_element(locator, timeout=timeout)
        try:
            element.click()
            self.logger.info(f"click element: {locator}")
        except Exception as e:
            self.logger.error(f"click element fail: {locator}, error: {str(e)}")
            raise


    def send_keys(self, locator, text, clear_first=True, timeout=None):
        """
        输入文本
        """
        element = self.find_element(locator, timeout=timeout)
        try:
            if clear_first:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"element: {locator} input: {text}")
        except Exception as e:
            self.logger.error(f"element: {locator} input fail, error: {str(e)}")
            raise


    def get_text(self, locator, timeout=None):
        """
        获取元素文本
        """
        element = self.find_element(locator, timeout=timeout)
        return element.text


    def wait_for_element_visible(self, locator, timeout=None):
        """
        等待元素可见
        """
        wait_time = timeout if timeout is not None else self.timeout
        by, value = locator
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            self.logger.error(f"wait for element timeout ({wait_time}s): {locator}")
            raise # 直接抛出异常，让调用者处理


    def is_element_present(self, locator, timeout=None):
        """
        检查元素是否存在（不一定可见）
        """
        try:
            self.find_element(locator, timeout=timeout)
            return True
        except NoSuchElementException:
            return False


    def app_back(self):
        """返回上一页"""
        self.driver.back()
        self.logger.info("back to previous page")


    def back_and_wait_for_element(self, expected_locator, timeout=None):
        """
        执行返回操作，然后等待直到期望的元素出现。
        :param expected_locator: 返回后，期望在新页面上看到的元素的定位器。
        :param timeout: 等待期望元素出现的超时时间。
        """
        self.logger.info(f"back to previous page，wait for element: '{expected_locator}' show up...")
        self.driver.app_back()
        try:
            # 等待期望的元素可见，以确认页面已成功返回
            self.wait_for_element_visible(expected_locator, timeout)
            self.logger.info("back to previous page success, and find the expected element")
        except TimeoutException:
            self.logger.error(f"back to previous page success，but can not find the expected element: {expected_locator}")
            raise
            # 抛出异常，让测试失败，因为没有返回到正确的页面

