import time
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.MainPages import MainPage

class PageLoginMP(MainPage):

    PASSWORD_NUMBER_ALL = [(By.XPATH, '//android.view.View[@content-desc="zero"]'),
                           (By.XPATH, '//android.view.View[@content-desc="one"]'),
                           (By.XPATH, '//android.view.View[@content-desc="two"]'),
                           (By.XPATH, '//android.view.View[@content-desc="three"]'),
                           (By.XPATH, '//android.view.View[@content-desc="four"]'),
                           (By.XPATH, '//android.view.View[@content-desc="five"]'),
                           (By.XPATH, '//android.view.View[@content-desc="six"]'),
                           (By.XPATH, '//android.view.View[@content-desc="seven"]'),
                           (By.XPATH, '//android.view.View[@content-desc="eight"]'),
                           (By.XPATH, '//android.view.View[@content-desc="nine"]'),
                           (By.XPATH, '//android.view.View[@content-desc="zero"]'),
                           (By.XPATH, '//android.view.View[@content-desc="zero"]')
                           ]
    FIO_KM = (By.XPATH, '//android.widget.TextView[@content-desc="ФИО КМ"]')
    HELP_ABOUT_PROGRAM = (By.XPATH, '//android.widget.TextView[@content-desc="Справка"]')
    HELP_ABOUT_PROGRAM_TITLE = (By.XPATH, '//android.widget.TextView[@content-desc="Справка о программе"]')
    ABOUT_PROGRAM = (By.XPATH, '//android.widget.TextView[@content-desc="О программе"]')
    VERSION_MP = (By.XPATH, '//android.widget.TextView[@content-desc="Версия МП"]')
    ACCESS_IS_DENIED = (By.XPATH, '//android.widget.TextView[@content-desc="Сообщение: Доступ запрещен"]')
    ERROR_ACCESSING_SERVER = (By.XPATH, '//android.widget.TextView[@content-desc="Ошибка при обращении к серверу"]')
    # ERROR_ACCESSING_SERVER_NEW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.TextView[1]')
    ERROR_INCORRECT_PASSWORD = (By.XPATH, '//android.widget.TextView[@content-desc="Вы ввели неверный пароль"]')
    PASSWORD_CLEAR = (By.XPATH, '//android.view.View[@content-desc="clear"]')
    INDICATOR_WHITE_1 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №1 - белый"]')
    INDICATOR_WHITE_2 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №2 - белый"]')
    INDICATOR_WHITE_3 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №3 - белый"]')
    INDICATOR_WHITE_4 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №4 - белый"]')
    INDICATOR_RED_1 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №1 - белый"]')
    INDICATOR_RED_2 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №2 - белый"]')
    INDICATOR_RED_3 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №3 - белый"]')
    INDICATOR_RED_4 = (By.XPATH, '//android.view.View[@content-desc="Индикатор №4 - белый"]')
    VERSION_MP_TEXT = 'Версия 4.2.16, база TBB-k15'
    INDICATOR_WHITE = 'белый'
    INDICATOR_RED = 'красный'

    @allure.step
    def login_km(self, base, km_password):
        """Открывает страницу поиск клиента, указать селектор базы"""
        self.base_change(base)
        time.sleep(0.1)
        self.sig_in(km_password)

    @allure.step
    def base_change(self, selector):
        self.click_element(self.VERSION_MP)
        self.click_element(self.BASE)
        self.logger.info(f"BASE selector = {selector}")
        self.click_element(selector)
        # assert self.field_presence_check(self.PASSWORD_ONE, wait_time=20)

    def iterate_all_numbers(self):
        """Перебираем все цифры, нажимаем и удаляем"""
        number_password = 0
        for step in range(3):
            self.logger.info(f"Начало ввода нового пароля")
            for number_indicator in range(4):
                self.click_element(self.PASSWORD_NUMBER_ALL[number_password])
                number_password += 1

    def select_and_delete_numbers(self):
        for number in self.PASSWORD_NUMBER_ALL:
            self.click_element(number)
            self.field_presence_check(self.INDICATOR_RED_1, wait_time=0.01)
            self.click_element(self.PASSWORD_CLEAR)
            self.field_presence_check(self.INDICATOR_WHITE_1, wait_time=0.01)

