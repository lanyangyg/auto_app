from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CheckoutCompletePage(BasePage):
    # 元素定位器
    CONTINUE_SHOPPING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Continue Shopping button')          # 继续购物按钮
    CHECKOUT_COMPLETE_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Checkout Complete"]')                 # 下单完成文案


    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def is_checkout_complete(self):
        # 验证是否出现下单完成标志
        return self.is_element_present(self.CHECKOUT_COMPLETE_TEXT)


    def continue_shopping(self):
        # 点击继续购物
        self.click(self.CONTINUE_SHOPPING_BUTTON)