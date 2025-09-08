from bases import base_page
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(base_page.BasePage):
    """
    登录页面
    """
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Username input field')        # 用户名输入框
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Password input field')        # 密码输入框
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Login button')                  # 登录按钮
    ERROR_MESSAGE = (AppiumBy.XPATH, '//*[@content-desc="generic-error-message"]/android.widget.TextView')    # 报错信息
    PRODUCT_HEADER = (AppiumBy.XPATH, '//*[@content-desc="container header"]/android.widget.TextView')        # 首页products标题

    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def is_on_login_page(self, timeout=2):
        """
        检查是否在登录页面
        """
        try:
            self.wait_for_element_visible(self.USERNAME_FIELD, timeout=timeout)
            return True
        except:
            # 捕获所有可能的异常（如TimeoutException）
            return False


    def login(self, username, password):
        """
        登录
        """
        self.wait_for_element_visible(self.USERNAME_FIELD)
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)


    def verify_login_success(self, timeout):
        """
        检查登录成功
        """
        return self.is_element_present(self.PRODUCT_HEADER, timeout=timeout)


    def verify_login_fail(self):
        """
        检查登录失败并返回错误消息
        """
        error_element = self.wait_for_element_visible(self.ERROR_MESSAGE)
        # 如果找到了元素（不是 None），就返回它的文本；否则返回一个清晰的提示
        if error_element:
            return error_element.text
        return "error：can not find the error message"
