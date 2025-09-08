from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ProductDetailsPage(BasePage):
    # 元素定位器
    COUNTER_PLUS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'counter plus button')                # 增加商品数量按钮
    COUNTER_MINS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'counter minus button')               # 减少商品数量按钮
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button')                  # 加入购物车按钮


    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def product_counter_plus(self):
        self.click(self.COUNTER_PLUS_BUTTON)

    def product_counter_mins(self):
        self.click(self.COUNTER_MINS_BUTTON)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

