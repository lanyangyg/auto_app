import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


# 注册所有模块化的fixture
pytest_plugins = ["fixtures.ui_setup_fixtures"]

@pytest.fixture(scope="session")
def appium_driver():
    """
    Session作用域的driver，整个测试过程只启动和退出一次APP
    """
    # 创建 Appium对象
    appium_server_url = 'http://127.0.0.1:4723'
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "16",
        "appium:deviceName": "Medium Phone API 36.0",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/Finn/Downloads/Android-MyDemoAppRN.1.3.0.build-244.apk",
        "appium:appPackage": "com.saucelabs.mydemoapp.rn",
        "appium:appActivity": ".MainActivity",
        "appium:autoGrantPermissions": True,    # 自动处理权限
        "appium:newCommandTimeout": 60          # 1分钟无命令则超时
    })
    # 初始化驱动
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)      # 使用options参数
    driver.implicitly_wait(5)       # 隐式等待
    yield driver
    driver.quit()
