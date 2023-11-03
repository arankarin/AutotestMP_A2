import allure
from selenium.webdriver.common.by import By

from page_objects.MainPages import MainPage

class ClientSearch(MainPage):

    # Страница Поиск клиента (по нажатию "Добавить")
    CLIENT_SURNAME = (By.XPATH, '//android.view.View[@content-desc="Фамилия"]/..')
    CLIENT_NAME = (By.XPATH, '//android.view.View[@content-desc="Имя"]/..')
    PATRONYMIC_TEXTVIEV_PARENT = (By.XPATH, '//android.view.View[@content-desc="Отчество"]/..')
    DATE_OF_BIRTH_TEXTVIEV_PARENT = (By.XPATH, '//android.view.View[@content-desc="Дата рождения"]/..')
    PHONE_NUMBER_TEXTVIEV_PARENT = (By.XPATH, '//android.view.View[@content-desc="Номер телефона"]/..')
    FIND_CLIENT_BUTTON_PARENT = (By.XPATH, '//android.view.View[@content-desc="Кнопка Создать клиента"]')
    # GENERAL_INFORMATION = (By.XPATH, '//android.widget.TextView[@content-desc="Общая информация"]')
    # PHONE_NUMBER_VALIDATIONS = (By.XPATH, '//android.widget.TextView[@content-desc="Номер телефона валидация"]')

    SURNAME_TEXT = 'Тестфамилия'
    NAME_TEXT = 'Тестимя'
    PATRONYMIC_TEXTVIEV_PARENT_TEXT = 'Тестотчество'
    DATE_OF_BIRTH_TEXT = '01012000'
    PHONE_NUMBER_TEXT = '79310000006'

    # SURNAME_TEXT = 'Тестфамилия'
    # NAME_TEXT = 'Изменение'
    # PATRONYMIC_TEXTVIEV_PARENT_TEXT = 'Существующего'
    # DATE_OF_BIRTH_TEXT = '01012000'
    # PHONE_NUMBER_TEXT = '79310000007'
    #
    # SURNAME_TEXT = 'Тестфамилия'
    # NAME_TEXT = 'Заявка'
    # PATRONYMIC_TEXTVIEV_PARENT_TEXT = 'Тестотчество'
    # DATE_OF_BIRTH_TEXT = '01012000'
    # PHONE_NUMBER_TEXT = '79310000008'
