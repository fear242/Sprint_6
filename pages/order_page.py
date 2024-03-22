import allure
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем форму "Для кого самокат"')
    def fulfill_personal_data_form(self, name_field, name, family_name_field, family_name, address_field, address,
                                   metro_field, metro_station, phone_number_field, phone):
        self.text_input_to_element(name_field, name)
        self.text_input_to_element(family_name_field, family_name)
        self.text_input_to_element(address_field, address)
        self.click_on_element(metro_field)
        self.click_on_element(metro_station)
        self.text_input_to_element(phone_number_field, phone)

    @allure.step('Заполняем форму "Про аренду"')
    def fulfill_rental_data_form(self, date_field, date, rental_period_field, rental_period_selector, color,
                                 button_order_in_middle):
        self.click_on_element(date_field)
        self.click_on_element(date)
        self.click_on_element(rental_period_field)
        self.click_on_element(rental_period_selector)
        self.click_on_element(color)
        self.click_on_element(button_order_in_middle)

    @allure.step('Проверяем, что всплыло окно "Заказ оформлен"')
    def check_order(self, locator):
        return self.find_element_with_wait(locator)
