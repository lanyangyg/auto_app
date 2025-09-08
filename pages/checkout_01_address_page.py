from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.checkout_02_payment_page import CheckoutPaymentPage

class CheckoutAddressPage(BasePage):
    # 元素定位器
    FULL_NAME_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')                       # 姓名输入框
    ADDRESS_INPUT_LINE_ONE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field')     # 地址第一行输入框
    ADDRESS_INPUT_LINE_TWO_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Address Line 2 input field')     # 地址第二行输入框
    CITY_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'City* input field')                                 # 城市输入框
    STATE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'State/Region input field')                         # 省份输入框
    ZIP_CODE_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Zip Code* input field')                         # 邮编输入框
    COUNTRY_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'Country* input field')                           # 国家输入框
    TO_PAYMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'To Payment button')                                # 去支付按钮


    def __init__(self, appium_driver):
        super().__init__(appium_driver)


    def enter_address_info(self, shipping_name, address_one, address_two, city, state, zipcode, country):
        # 填写地址信息
        self.send_keys(self.FULL_NAME_INPUT_FIELD, shipping_name)
        self.send_keys(self.ADDRESS_INPUT_LINE_ONE_INPUT_FIELD, address_one)
        self.send_keys(self.ADDRESS_INPUT_LINE_TWO_INPUT_FIELD, address_two)
        self.send_keys(self.CITY_INPUT_FIELD, city)
        self.send_keys(self.STATE_INPUT_FIELD, state)
        self.send_keys(self.ZIP_CODE_INPUT_FIELD, zipcode)
        self.send_keys(self.COUNTRY_INPUT_FIELD, country)

    def to_payment(self):
        # 点击去支付按钮
        self.click(self.TO_PAYMENT_BUTTON)
        # 保证跳到payment页
        self.wait_for_element_visible(CheckoutPaymentPage.CARD_NUMBER_INPUT_FIELD)