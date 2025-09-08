from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CheckoutReviewPage(BasePage):
    # 元素定位器
    PLACE_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Place Order button')              # 下单按钮
    TOTAL_NUMBER = (AppiumBy.ACCESSIBILITY_ID, 'total number')                          # 总商品数量text
    TOTAL_PRICE = (AppiumBy.ACCESSIBILITY_ID, 'total price')                            # 总商品价格text


    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def product_total_number(self):
        # 返回总商品数量text
        self.get_text(self.TOTAL_NUMBER)

    def product_total_price(self):
        # 返回总商品价格text
        self.get_text(self.TOTAL_PRICE)

    def place_order(self):
        # 点击下单按钮
        self.click(self.PLACE_ORDER_BUTTON)