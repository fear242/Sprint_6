import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Открываем страницу заказа и соглашаемся с cookies')
    def open_order_paige_confirm_cookies(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        self.click_on_element(MainPageLocators.BUTTON_COOKIES)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fulfill_personal_data_form(self, name, family_name, address, phone):
        self.text_input_to_element(OrderPageLocators.NAME_FIELD, name)
        self.text_input_to_element(OrderPageLocators.FAMILY_NAME_FIELD, family_name)
        self.text_input_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(OrderPageLocators.METRO_STATION)
        self.text_input_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, phone)

    @allure.step('Заполняем форму "Про аренду"')
    def fulfill_rental_data_form(self):
        self.click_on_element(OrderPageLocators.DATE_FIELD)
        self.click_on_element(OrderPageLocators.DATE_BUTTON)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_SELECTOR)
        self.click_on_element(OrderPageLocators.COLOR)
        self.click_on_element(MainPageLocators.BUTTON_ORDER_IN_MIDDLE)

    @allure.step('Проверяем, что всплыло окно "Заказ оформлен"')
    def check_order(self):
        return self.find_element_with_wait(OrderPageLocators.MODAL_ORDER_PLACED)

    @allure.step('Скроллим до кнопки "Далее" и жмём её')
    def scroll_and_click_next_button(self):
        self.scroll_to_element(OrderPageLocators.BUTTON_NEXT)
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Жмём кнопку "Да", подтверждая заказ')
    def click_to_confirm_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step('Клик по логотипу Самокат')
    def cllick_on_samokat_logo(self):
        self.click_on_element(MainPageLocators.HEADER_SCOOTER_LOGO)
