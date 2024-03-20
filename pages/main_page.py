from pages.base_page import BasePage


class MainPage(BasePage):

    def get_text_from_answer(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def fulfill_personal_data_form(self, name_field, name, family_name_field, family_name, address_field, address,
                                   metro_field, metro_station, phone_number_field, phone, button_next):
        self.text_input_to_element(name_field, name)
        self.text_input_to_element(family_name_field, family_name)
        self.text_input_to_element(address_field, address)
        self.click_on_element(metro_field)
        self.click_on_element(metro_station)
        self.text_input_to_element(phone_number_field, phone)
        self.click_on_element(button_next)

    def fulfill_rental_data_form(self, date_field, date, rental_period_field, rental_period_selector, color,
                                 button_order_in_middle):
        self.click_on_element(date_field)
        self.click_on_element(date)
        self.click_on_element(rental_period_field)
        self.click_on_element(rental_period_selector)
        self.click_on_element(color)
        self.click_on_element(button_order_in_middle)

    def check_order(self, locator):
        self.get_text_from_element(locator)
