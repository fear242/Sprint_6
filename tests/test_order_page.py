import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import UserData


class TestOrderPage:

    @pytest.mark.parametrize(
        'button_order_locator, name, family_name, address, phone',
        [
            (MainPageLocators.BUTTON_ORDER_IN_MIDDLE, UserData.name_1, UserData.family_name_1, UserData.address_1, UserData.phone_1),
            (MainPageLocators.BUTTON_ORDER_HEADER, UserData.name_2, UserData.family_name_2, UserData.address_2, UserData.phone_2)
        ]
    )
    @allure.title('Проверка позитивного сценария заказа')
    def test_making_order_positive(self, driver, button_order_locator, name, family_name, address, phone):
        order_page = OrderPage(driver)
        order_page.open_paige_confirm_cookies('https://qa-scooter.praktikum-services.ru/')
        order_page.click_on_element(button_order_locator)
        order_page.fulfill_personal_data_form(name, family_name, address, phone)
        order_page.scroll_and_click_next_button()
        order_page.fulfill_rental_data_form()
        order_page.click_to_confirm_order()
        assert order_page.check_order().is_displayed
