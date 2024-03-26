# Sprint_6
Final project of sixth sprint on "Python QA automation" course.
Structure:
Sprint_6/
├-locators
│  ├-main_page_locators.py - Локаторы элементов главной страницы тестируемого сайта и dzen 
│  └-order_page_locators.py - Локаторы элементов страницы оформления заказа
├-pages
│  ├-base_page.py - Базовые методы взаимодействия драйвера с элементами страниц
│  ├-main_page.py - Методы для взаимодействия с элементами главной страницы
│  └-order_page.py - Методы для взаимодействия с элементами страницы заказа
├-tests
│  ├-test_main_page.py - Проверка соответствия текстов ответов вопросам
│  ├-test_order_page.py - Проверка позитивного сценария заказа с двумя наборами данных с разными точками входа
│  └-test_transfers.py - Проверка переходов по клику на логотипы Яндекс и Самокат
├-allure_results - Отчёты о тестах
├-conftest.py - Фикстура инициализации драйвера Firefox
├-data.py - Наборы текстов ответов и тестовых данных для оформления заказа
├-README.md - Этот файл
└-requirements.txt - Внешние зависимости
