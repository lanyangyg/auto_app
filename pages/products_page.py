from selenium.common import NoSuchElementException
from bases.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ProductsPage(BasePage):
    """
    产品列表页面
    """
    # 元素定位器
    PRODUCT_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, 'products screen')      # 商品容器
    PRODUCT_NAME = (AppiumBy.ACCESSIBILITY_ID, "store item text")           # 商品名称
    PRODUCT_PRICE = (AppiumBy.ACCESSIBILITY_ID, "store item price")         # 商品价格
    PRODUCT_IMAGE = (AppiumBy.CLASS_NAME, "android.widget.ImageView")       # 商品图片
    PRODUCT_HEADER = (AppiumBy.XPATH, '//*[@content-desc="container header"]/android.widget.TextView')         # 首页products标题

    def __init__(self, appium_driver):
        """
        构造函数，传appium_driver驱动，继承BasePage父类的所有方法
        """
        super().__init__(appium_driver)


    def get_all_product_containers(self):
        """
        获取所有商品的父容器
        """
        return self.find_elements(self.PRODUCT_CONTAINER)


    def get_product_details_list(self):
        """
        遍历所有商品，提取名称和价格，返回一个字典列表。
        例如: [{'name': 'Sauce Labs Backpack', 'price': '$29.99'}, ...]
        """
        product_containers = self.get_all_product_containers()
        # 定义一个空列表，可以使用 append()方法将每个商品添加到列表中
        product_item = []

        # 遍历商品并添加到列表
        for container in product_containers:
            try:
                product_name = container.find_element(*self.PRODUCT_NAME).text
                product_price = container.find_element(*self.PRODUCT_PRICE).text
                product_item.append({"product_name":product_name, "product_prince":product_price})
            except Exception as e:
                print(f"making mistake to get product: {e}")


    def click_product_by_name(self, target_product_name, click_target='name'):      # click_target默认参数值是name，testcase调用时也可以传image
        """
        点击指定的商品
        """
        product_containers = self.get_all_product_containers()
        # 遍历这些容器，在每个容器里找到商品名称
        for container in product_containers:
            try:
                # 在每个容器内部查找商品名称
                name_element = container.find_element(*self.PRODUCT_NAME)
                # 检查每个容器内的商品名与传进去的目标商品名是否匹配
                if name_element.text == target_product_name:
                    self.logger.info(f"find target product: '{target_product_name}'")

                    if click_target == 'image':
                        # 如果要点击商品图片就执行以下操作
                        target_element = container.find_element(*self.PRODUCT_IMAGE)
                        self.logger.info("ready to click product image")
                    else:
                        # 否则默认点击名称元素
                        target_element = name_element
                        self.logger.info("ready to click product name")

                    target_element.click()
                    # 找到并点击后，结束循环和方法
                    return

            except NoSuchElementException:
                # 如果某个容器里没有找到名称元素，就跳过它继续找下一个
                continue

        # 如果循环结束了还没找到，就抛出异常
        raise NoSuchElementException(f"can not find the target:'{target_product_name}'")


    def is_on_product_page(self, timeout=None):
        """
        检查当前位于product page，返回True或False
        """
        return self.is_element_present(self.PRODUCT_HEADER, timeout=timeout)