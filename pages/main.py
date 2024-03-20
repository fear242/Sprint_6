from pages.base_page import BasePage


class MainPage(BasePage):

    def get_text_from_answer(self, locator_q, locator_a):
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    def fulfill_personal_data_form(self, name_field, name, family_name_field, family_name, address_field, address,
                                   metro_field, metro_station, button_next):
        self.text_input_to_element(name_field, name)
        self.text_input_to_element(family_name_field, family_name)
        self.text_input_to_element(address_field, address)
        self.click_on_element(metro_field)
        self.click_on_element(metro_station)
        self.click_on_element(button_next)

    def fulfill_rental_data_form(self, date_field, date, rental_period_field, rental_period, color, comment_field,
                                 comment_text, button_make_order):
        self.click_on_element(date_field)
        self.click_on_element(date)
        self.click_on_element(rental_period_field)
        self.click_on_element(rental_period)
        self.click_on_element(color)
        self.text_input_to_element(comment_field, comment_text)
        self.click_on_element(button_make_order)

    def check_order(self, locator):
        self.get_text_from_element(locator)
