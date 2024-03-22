import pytest
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
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
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page.click_on_element(MainPageLocators.BUTTON_COOKIES)
        order_page.click_on_element(button_order_locator)
        order_page.fulfill_personal_data_form(OrderPageLocators.NAME_FIELD, name, OrderPageLocators.FAMILY_NAME_FIELD,
                                              family_name, OrderPageLocators.ADDRESS_FIELD, address,
                                              OrderPageLocators.METRO_FIELD, OrderPageLocators.METRO_STATION,
                                              OrderPageLocators.PHONE_NUMBER_FIELD, phone)
        order_page.scroll_to_element(OrderPageLocators.BUTTON_NEXT)
        order_page.click_on_element(OrderPageLocators.BUTTON_NEXT)
        order_page.fulfill_rental_data_form(OrderPageLocators.DATE_FIELD, OrderPageLocators.DATE_TOMORROW,
                                            OrderPageLocators.RENTAL_PERIOD_FIELD, OrderPageLocators.RENTAL_PERIOD_SELECTOR,
                                            OrderPageLocators.COLOR, MainPageLocators.BUTTON_ORDER_IN_MIDDLE)
        order_page.click_on_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)
        assert order_page.check_order(OrderPageLocators.MODAL_ORDER_PLACED).is_displayed
