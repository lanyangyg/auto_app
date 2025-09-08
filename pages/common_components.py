from selenium.common import TimeoutException
from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage


class CommonComponents(BasePage):
    """
    管理APP中的通用组件，如侧边栏菜单、全局弹窗
    """
    # --- 定位器 ---
    CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'cart badge')                     # 购物车组件
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'open menu')                      # 菜单组件
    CATALOG_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'menu item catalog')        # 菜单下的产品目录
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'menu item log in')           # 菜单下的登录选项
    LOGOUT_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'menu item log out')         # 菜单下的登出选项
    GO_SHOPPING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Go Shopping button')      # 购物车页面的去购物按钮
    LOGOUT_CONFIRM_BUTTON = (AppiumBy.XPATH, "//*[@text='LOG OUT']")            # 登出流程中第一个弹窗按钮
    LOGOUT_OK_BUTTON = (AppiumBy.XPATH, "//*[@text='OK']")                      # 登出流程中第二个弹窗按钮

    def __init__(self, appium_driver):
        super().__init__(appium_driver)

    def is_user_logged_in_by_navigation(self):
        """
        通过点击'Log In'菜单项后的跳转页面来判断登录状态
        跳转到购物车 -> 已登录 (True)
        跳转到登录页 -> 未登录 (False)
        这个方法执行后，APP会停留在购物车页或登录页。
        """
        self.click(self.MENU_BUTTON)
        self.click(self.LOGIN_MENU_ITEM)
        try:
            self.wait_for_element_visible(self.GO_SHOPPING_BUTTON)
            return True
        except TimeoutException:
            return False


    def complete_logout(self):
        """
        执行完整的登出流程，包括处理所有弹窗
        """
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_MENU_ITEM)
        self.click(self.LOGOUT_CONFIRM_BUTTON)
        self.click(self.LOGOUT_OK_BUTTON)

    def navigate_to_login_page(self):
        """
        通过菜单导航到登录页
        """
        self.click(self.MENU_BUTTON)
        self.click(self.LOGIN_MENU_ITEM)


    def navigate_to_cart(self):
        """
        点击右上购物车角图标进入购物车页面
        """
        self.click(self.CART_BUTTON)


    def navigate_to_products_page(self):
        """
        通过菜单导航到产品列表页
        """
        self.click(self.MENU_BUTTON)
        self.click(self.CATALOG_MENU_ITEM)


    def ensure_user_is_logged_in(self, username, password):
        """
        确保用户处于登录状态。
        如果已登录，则什么都不做，直接返回产品页。
        如果未登录，则执行登录操作。
        """
        is_logged_in = self.is_user_logged_in_by_navigation()

        if is_logged_in:
            self.logger.info("用户已登录，返回产品页。")
            self.app_back()
            return
        self.logger.info("用户未登录，现在执行登录...")
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        # 登录后会自动跳转到产品页