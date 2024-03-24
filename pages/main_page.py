from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Кликаем по вопросу и получаем текст ответа')
    def get_text_from_answer(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Прокручиваем до блока с вопросами')
    def scroll_to_questions_block(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_BLOCK)

    @allure.step('Клик по логотипу Яндекс')
    def click_on_yandex_logo(self):
        self.click_on_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Переключаем фокус драйвера на новую вкладку')
    def switch_driver_to_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ищем кнопку "Найти"')
    def find_search_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_SEARCH)
