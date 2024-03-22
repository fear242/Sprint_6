import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import Results


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Results.result_0),
            (1, Results.result_1),
            (2, Results.result_2),
            (3, Results.result_3),
            (4, Results.result_4),
            (5, Results.result_5),
            (6, Results.result_6),
            (7, Results.result_7)
        ]
    )
    @allure.title('Проверка соответствия текста ответов вопросам')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_to_element(MainPageLocators.QUESTIONS_BLOCK)
        assert main_page.get_text_from_answer(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            num
        ) == result
