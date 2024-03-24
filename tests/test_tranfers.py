import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestTransfers:

    @allure.title('Проверка перехода на главную по клику на лого Самокат')
    def test_click_samokat_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_paige_confirm_cookies()
        order_page.cllick_on_samokat_logo()
        assert order_page.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на Дзен по клику на лого Яндекс')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_paige_confirm_cookies()
        main_page.click_on_yandex_logo()
        main_page.switch_driver_to_tab()
        main_page.find_search_button()
        assert main_page.driver.current_url == 'https://dzen.ru/?yredirect=true'
