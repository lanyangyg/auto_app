import pytest
from events.complete_order_event import CompleteOrderFlow


@pytest.mark.usefixtures("logged_in_state_fixture")
class TestOrderEvent:
    def test_order_event(self, appium_driver):
        complete_order = CompleteOrderFlow(appium_driver)
        complete_order.complete_order_flow()
        assert complete_order.checkout_complete_page.is_checkout_complete()
