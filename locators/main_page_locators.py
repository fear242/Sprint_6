from selenium.webdriver.common.by import By


class MainPageLocators:

    HEADER_SCOOTER_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoScooter_")]'
    HEADER_YANDEX_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoYandex_")]'
    BUTTON_ORDER_IN_MIDDLE = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Заказать"]'
    BUTTON_ORDER_HEADER = By.XPATH, '//*[contains(@class, "Header_Nav")]/child::button[text()="Заказать"]'
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    NAME_FIELD = By.XPATH, '//*[contains(@placeholder, "Имя")]'
    FAMILY_NAME_FIELD = By.XPATH, '//*[contains(@placeholder, "Фамилия")]'
    ADDRESS_FIELD = By.XPATH,'//*[contains(@placeholder, "Адрес")]'
    METRO_FIELD = By.XPATH, '//*[contains(@placeholder, "метро")]'
    METRO_STATION = By.XPATH, '//*[@class="select-search__row"]'
    PHONE_NUMBER_FIELD = By.XPATH, '//*[contains(@placeholder, "Телефон")]'
    BUTTON_NEXT = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Далее"]'
    DATE_FIELD = By.XPATH, '//*[contains(@placeholder, "Когда")]'
    DATE_TOMORROW = By.XPATH, '//*[contains(@class, "today")]/following-sibling::div'
    DATE_YESTERDAY = By.XPATH, '//*[contains(@class, "today")]/preceding-sibling::div'
    RENTAL_PERIOD_FIELD = By.XPATH, '//*[contains(text(), "Срок аренды")]'
    RENTAL_PERIOD_SELECTOR = By.XPATH, '//*[@class="Dropdown-option"]'
    COLOR = By.XPATH, '//*[@id="black"]'
    BUTTON_CONFIRM_ORDER = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Да"]'



