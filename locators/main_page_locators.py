from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_COOKIES = By.XPATH, '//*[contains(@class, "App_CookieButton_")]'
    HEADER_SCOOTER_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoScooter_")]'
    HEADER_YANDEX_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoYandex_")]'
    BUTTON_ORDER_IN_MIDDLE = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Заказать"]'
    BUTTON_ORDER_HEADER = By.XPATH, '//*[contains(@class, "Header_Nav")]/child::button[text()="Заказать"]'
    QUESTIONS_BLOCK = By.XPATH, '//*[@class="accordion"]'
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'
    BUTTON_SEARCH = By.XPATH, '//*[text()="Найти"]'  # Кнопка в поисковой строке на dzen.ru
