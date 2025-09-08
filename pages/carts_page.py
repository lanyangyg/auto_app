from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CartPage(BasePage):
    # 元素定位
    GO_SHOPPING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Go Shopping button')                  # 购物车页面的去购物按钮
    REMOVE_ITEM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'remove item')                         # 移除商品按钮
    PROCEED_TO_CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Proceed To Checkout button')  # 结帐按钮
    TOTAL_NUMBER = (AppiumBy.ACCESSIBILITY_ID, 'total number')                              # 总商品数量text
    TOTAL_PRICE = (AppiumBy.ACCESSIBILITY_ID, 'total price')                                # 总商品价格text
    COUNTER_PLUS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'counter plus button')                # 增加商品数量
    COUNTER_MINS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'counter minus button')               # 减少商品数量

    def __init__(self, appium_driver):
        """
        构造函数
        """
        super().__init__(appium_driver)

    def is_cart_empty(self):
        """
        通过检查“GO_SHOPPING_BUTTON”按钮是否存在来判断购物车是否为空
        """
        cart_empty = self.is_element_present(self.GO_SHOPPING_BUTTON, timeout=3)
        return cart_empty


    def empty_cart(self):
        """
        循环点击“REMOVE_ITEM_BUTTON”按钮来清空购物车
        """
        print("empty_cart ing...")
        while self.is_element_present(self.REMOVE_ITEM_BUTTON, timeout=2):
            # while循环，只要条件为true，重复执行
            self.click(self.REMOVE_ITEM_BUTTON)


    def go_shopping_from_empty_cart(self):
        """
        在空购物车页面，点击"GO_SHOPPING_BUTTON"或者返回按钮返回产品列表
        """
        if self.is_cart_empty():
            self.click(self.GO_SHOPPING_BUTTON)
        else:
            self.app_back()


    def proceed_to_checkout(self):
        """
        点击"PROCEED_TO_CHECKOUT_BUTTON"结帐
        """
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)


    def cart_counter_plus(self):
        # 增加商品数量
        self.click(self.COUNTER_PLUS_BUTTON)

    def cart_counter_mins(self):
        # 减少商品数量
        self.click(self.COUNTER_MINS_BUTTON)

    def cart_total_number(self):
        # 返回总商品数量
        return self.find_element(self.TOTAL_NUMBER).text

    def cart_total_price(self):
        # 返回总商品价格
        return self.find_element(self.TOTAL_PRICE).text
