import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import Results, UserData


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
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_to_element(MainPageLocators.QUESTIONS_BLOCK)
        assert main_page.get_text_from_answer(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            num
        ) == result

    @pytest.mark.parametrize(
        'button_order_locator, name, family_name, address, phone',
        [
            (MainPageLocators.BUTTON_ORDER_IN_MIDDLE, UserData.name_1, UserData.family_name_1, UserData.address_1, UserData.phone_1),
            (MainPageLocators.BUTTON_ORDER_HEADER, UserData.name_2, UserData.family_name_2, UserData.address_2, UserData.phone_2)
        ]
    )
    def test_making_order_positive(self, driver, button_order_locator, name, family_name, address, phone):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_element(MainPageLocators.BUTTON_COOKIES)
        main_page.click_on_element(button_order_locator)
        main_page.fulfill_personal_data_form(MainPageLocators.NAME_FIELD, name, MainPageLocators.FAMILY_NAME_FIELD,
                                             family_name, MainPageLocators.ADDRESS_FIELD, address,
                                             MainPageLocators.METRO_FIELD, MainPageLocators.METRO_STATION,
                                             MainPageLocators.PHONE_NUMBER_FIELD, phone)
        main_page.scroll_to_element(MainPageLocators.BUTTON_NEXT)
        main_page.click_on_element(MainPageLocators.BUTTON_NEXT)
        main_page.fulfill_rental_data_form(MainPageLocators.DATE_FIELD, MainPageLocators.DATE_TOMORROW,
                                           MainPageLocators.RENTAL_PERIOD_FIELD, MainPageLocators.RENTAL_PERIOD_SELECTOR,
                                           MainPageLocators.COLOR, MainPageLocators.BUTTON_ORDER_IN_MIDDLE)
        main_page.click_on_element(MainPageLocators.BUTTON_CONFIRM_ORDER)
        assert main_page.check_order(MainPageLocators.MODAL_ORDER_PLACED).is_displayed

    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        main_page.click_on_element(MainPageLocators.HEADER_SCOOTER_LOGO)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_element(MainPageLocators.HEADER_YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        main_page.find_element_with_wait(MainPageLocators.BUTTON_SEARCH)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
