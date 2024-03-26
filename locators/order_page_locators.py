from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = By.XPATH, '//*[contains(@placeholder, "Имя")]'
    FAMILY_NAME_FIELD = By.XPATH, '//*[contains(@placeholder, "Фамилия")]'
    ADDRESS_FIELD = By.XPATH, '//*[contains(@placeholder, "Адрес")]'
    METRO_FIELD = By.XPATH, '//*[contains(@placeholder, "метро")]'
    METRO_STATION = By.XPATH, '//*[@class="select-search__row"]'
    PHONE_NUMBER_FIELD = By.XPATH, '//*[contains(@placeholder, "Телефон")]'
    BUTTON_NEXT = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Далее"]'
    DATE_FIELD = By.XPATH, '//*[contains(@placeholder, "Когда")]'
    DATE_BUTTON = By.XPATH, '//*[contains(@class, "today")]'
    RENTAL_PERIOD_FIELD = By.XPATH, '//*[contains(text(), "Срок аренды")]'
    RENTAL_PERIOD_SELECTOR = By.XPATH, '//*[@class="Dropdown-option"]'
    COLOR = By.XPATH, '//*[@id="black"]'
    BUTTON_CONFIRM_ORDER = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Да"]'
    MODAL_ORDER_PLACED = By.XPATH, '//*[contains(@class, "Order_Modal_")]'
