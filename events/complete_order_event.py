from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.producet_details_page import ProductDetailsPage
from pages.carts_page import CartPage
from pages.checkout_01_address_page import CheckoutAddressPage
from pages.checkout_02_payment_page import CheckoutPaymentPage
from pages.checkout_03_review_page import CheckoutReviewPage
from pages.checkout_04_complete_page import CheckoutCompletePage
from pages.common_components import CommonComponents


class CompleteOrderFlow:
    def __init__(self,appium_driver):
        self.common_components = CommonComponents(appium_driver)
        self.product_page = ProductsPage(appium_driver)
        self.product_details_page = ProductDetailsPage(appium_driver)
        self.cart_page = CartPage(appium_driver)
        self.login_page = LoginPage(appium_driver)
        self.checkout_address_page = CheckoutAddressPage(appium_driver)
        self.checkout_payment_page = CheckoutPaymentPage(appium_driver)
        self.checkout_review_page = CheckoutReviewPage(appium_driver)
        self.checkout_complete_page = CheckoutCompletePage(appium_driver)

    def complete_order_flow(self):
        """
        一个完整的端到端：
        游客(logged in) -> 商品 -> 加购 -> 结算 -> 完成
        """
        # 产品页，点击商品进入商品详情页
        target_product_name = "Sauce Labs Backpack"
        self.product_page.click_product_by_name(target_product_name)
        # 详情页点击加入购物车
        self.product_details_page.product_counter_plus()
        self.product_details_page.add_to_cart()
        # 通用组件点击购物车图标
        self.common_components.navigate_to_cart()
        # 购物车页面点击结帐按钮
        self.cart_page.proceed_to_checkout()
        # # 未登录，完整登录流程
        # self.login_page.login("bob@example.com", "10203040")
        # 结算流程
        self.checkout_address_page.enter_address_info("LAN", "address one", "address two", "city", "state", "12345",
                                                 "country")
        self.checkout_address_page.to_payment()

        self.checkout_payment_page.enter_payment_info("LAN", "123412341234123", "1126", "123")
        self.checkout_payment_page.review_order()

        self.checkout_review_page.place_order()
