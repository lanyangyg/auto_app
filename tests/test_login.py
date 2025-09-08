import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("navigate_to_login_page_fixture")      # Pytest 会自动从 ui_setup_fixtures.py 文件中找到这个 fixture 并应用
class TestLogin:

    @pytest.mark.parametrize("username, password, expected", [
        ("bob@example.com", "1111", {"error": "Provided credentials do not match any user in this service."}),
        ("alice@example.com", "10203040", {"error": "Sorry, this user has been locked out."})
    ])
    def test_login_fail(self, appium_driver, username, password, expected):
        login_page = LoginPage(appium_driver)
        login_page.login(username, password)
        assert login_page.verify_login_fail() == expected["error"]

    @pytest.mark.parametrize("username, password, expected", [
        ("bob@example.com", "10203040", {"success": "Products"})
    ])
    def test_login_success(self, appium_driver, username, password, expected):
        login_page = LoginPage(appium_driver)
        login_page.login(username, password)
        assert login_page.verify_login_success(timeout=5)
