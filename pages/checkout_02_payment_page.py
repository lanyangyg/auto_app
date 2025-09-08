from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutPaymentPage(BasePage):
    # 元素定位器
    FULL_NAME_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')
    CARD_NUMBER_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Card Number* input field')
    EXPIRATION_DATE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Expiration Date* input field')
    SECURITY_CODE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Security Code* input field')
    REVIEW_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Review Order button')


    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def enter_payment_info(self, payment_name, card_number, expiration_date, security_code):
        # 输入支付信息
        self.send_keys(self.FULL_NAME_INPUT_FIELD, payment_name)
        self.send_keys(self.CARD_NUMBER_INPUT_FIELD, card_number)
        self.send_keys(self.EXPIRATION_DATE_INPUT_FIELD, expiration_date)
        self.send_keys(self.SECURITY_CODE_INPUT_FIELD, security_code)

    def review_order(self):
        # 点击查看订单按钮
        self.click(self.REVIEW_ORDER_BUTTON)