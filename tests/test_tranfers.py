import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestTransfers:

    @allure.title('Проверка перехода на главную по клику на лого Самокат')
    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        main_page.click_on_element(MainPageLocators.HEADER_SCOOTER_LOGO)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на Дзен по клику на лого Яндекс')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_element(MainPageLocators.HEADER_YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        main_page.find_element_with_wait(MainPageLocators.BUTTON_SEARCH)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
