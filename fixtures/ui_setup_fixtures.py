import pytest
from pages.common_components import CommonComponents

# 定义一个用于登录的标准测试账户
LOGIN_USERNAME = "bob@example.com"
LOGIN_PASSWORD = "10203040"

@pytest.fixture(scope="class")
def navigate_to_login_page_fixture(appium_driver):
    """
    【类级别Setup】在这个测试类的所有测试开始前，运行一次。
    负责导航到登录页面。
    """
    print("\n--- [Setup Fixture] Navigating to Login Page ---")
    common_comps = CommonComponents(appium_driver)
    common_comps.navigate_to_products_page()
    common_comps.navigate_to_login_page()


@pytest.fixture(scope="function")
def logged_in_state_fixture(appium_driver):
    """
    【可复用Setup】确保用户已登录的fixture。
    测试用例可以通过名字来“请求”这个fixture。
    """
    print("\n--- [Setup Fixture] Ensuring user is logged in ---")
    common_comps = CommonComponents(appium_driver)
    common_comps.ensure_user_is_logged_in(LOGIN_USERNAME, LOGIN_PASSWORD)