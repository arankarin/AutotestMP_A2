from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardClientAddress(MainPage):

    # Адреса Адрес регистрации, Фактический адрес проживания, Адрес места работы
    ENTER_ADDRESS = (By.XPATH, '//android.view.View[@content-desc="Введите адрес"]/..')
    ALL_REGISTRATION_ADDRESS = (By.XPATH, '//android.widget.TextView[@content-desc="Список адресов"]')
    BUTTON_SAVE_ADDRESS = (By.XPATH, '//android.view.View[@content-desc="Сохранить кнопка"]')
    BUTTON_SAVE_ADDRESS_2 = (By.XPATH, '//android.view.View[@content-desc="Кнопка Сохранить"]')

    # Адрес релистрации на родине
    # ADDRESS_HOMELAND_COUNTRY = (By.XPATH, '//android.widget.TextView[@content-desc="Страна"]')
    ADDRESS_HOMELAND_COUNTRY = (By.XPATH, '//android.widget.TextView[@content-desc=" Выбранный элемент"]')
    COUNTRY_TADJIKISTAN = (By.XPATH, '//android.widget.TextView[@content-desc="ТАДЖИКИСТАН"]')
    COUNTRY_FULL_ADDRESS = (By.XPATH, '//android.view.View[@content-desc="Введите адрес полностью:"]/..')

    # Заполение нового клиента
    REGISTRATION_ADDRESS_TEXT = 'г Санкт-Петербург, ул Народная, д 2'
    REGISTRATION_ADDRESS_TEXT_FIELD = '193079, г Санкт-Петербург, Невский р-н, ул Народная, д 2'

    REGISTRATION_ADDRESS_TEXT_NEW = 'г Санкт-Петербург, ул Народная, д 10'
    REGISTRATION_ADDRESS_TEXT_NEW_FIELD = '193079, г Санкт-Петербург, Невский р-н, ул Народная, д 10'

    ADDRESS_PLACE_WORK_TEXT = '195009, г Санкт-Петербург, Калининский р-н, Лесной пр-кт, д 1'
    ADDRESS_PLACE_WORK_TEXT_NEW = '194100, г Санкт-Петербург, Выборгский р-н, ул Литовская, д 4'

    FULL_ADDRESS_TEXT = 'Адрес на родине'
