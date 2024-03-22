from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Кликаем по вопросу и получаем текст ответа')
    def get_text_from_answer(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
