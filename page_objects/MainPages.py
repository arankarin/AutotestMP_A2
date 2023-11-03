import time
import random
import datetime
import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.mouse_button import MouseButton

class MainPage:
    FIO_KM_TEXT = 'Здравствуйте, Воробьёв Игорь КМ'
    FINGERPRINT_TEXT_FIELD = (By.XPATH, '//android.widget.TextView[@content-desc="Отпечаток пальца текст"]')
    FINGERPRINT_NO = (By.XPATH, '//android.view.View[@content-desc="Отпечаток пальца нет"]')
    FINGERPRINT_YES = (By.XPATH, '//android.view.View[@content-desc="Отпечаток пальца да"]')
    PASSWORD_VOROBEV = [(By.XPATH, '//android.view.View[@content-desc="one"]'),
                           (By.XPATH, '//android.view.View[@content-desc="one"]'),
                           (By.XPATH, '//android.view.View[@content-desc="one"]'),
                           (By.XPATH, '//android.view.View[@content-desc="one"]')]
    PASSWORD_VOROBEV_NEGATIVE = [(By.XPATH, '//android.view.View[@content-desc="one"]'),
                           (By.XPATH, '//android.view.View[@content-desc="two"]'),
                           (By.XPATH, '//android.view.View[@content-desc="three"]'),
                           (By.XPATH, '//android.view.View[@content-desc="four"]')]
    PASSWORD_ONE = (By.XPATH, '//android.view.View[@content-desc="one"]')
    PASSWORD_TWO = (By.XPATH, '//android.view.View[@content-desc="two"]')
    PASSWORD_THREE = (By.XPATH, '//android.view.View[@content-desc="three"]')
    PASSWORD_FOUR = (By.XPATH, '//android.view.View[@content-desc="four"]')
    PASSWORD_FIVE = (By.XPATH, '//android.view.View[@content-desc="five"]')
    PASSWORD_SIX = (By.XPATH, '//android.view.View[@content-desc="six"]')
    PASSWORD_SEVEN = (By.XPATH, '//android.view.View[@content-desc="seven"]')
    PASSWORD_EIGHT = (By.XPATH, '//android.view.View[@content-desc="eight"]')
    PASSWORD_NINE = (By.XPATH, '//android.view.View[@content-desc="nine"]')
    PASSWORD_ZERO = (By.XPATH, '//android.view.View[@content-desc="zero"]')
    # PASSWORD_VOROBEV = [(By.XPATH,'//android.widget.TextView[@content-desc="one"]'), (By.XPATH,'//android.widget.TextView[@content-desc="one"]'),
    #              (By.XPATH,'//android.widget.TextView[@content-desc="one"]'), (By.XPATH,'//android.widget.TextView[@content-desc="one"]')]
    ALL_TEXT_VIEW = ['Последние события', 'Мои клиенты', 'Всего: ', 'Добавить', 'Мои заявки', 'Онлайн заявки',
                 'Монитор должников', 'Мои отчеты', 'Мои показатели', 'Рабочий стол', 'Настройки', 'Калькулятор займов']
    MAIN_MENU = ['Мои клиенты', 'Последние события', 'Добавить', 'Мои заявки', 'Онлайн заявки',
                 'Монитор должников', 'Мои отчеты', 'Мои показатели', 'Калькулятор займов', 'Настройки']

    MAIN_PAGE = (By.XPATH, '//android.widget.TextView[@content-desc="Рабочий стол"]')
    HEADING_GENERAL_INFORMATION = (By.XPATH, '//android.widget.TextView[@content-desc="Общая информация"]')
    CLIENT_CARD_SURNAME = (By.XPATH, '//android.widget.TextView[@content-desc="Фамилия в карточке клиента"]')
    TOTAL_CLIENTS_VOROBEV = '254'
    TOTAL_CLIENTS_TORBO = '645'

    MENU_LATEST_EVENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Последние события"]/..')
    TEXT_LATEST_EVENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Последние события"]')
    MENU_MY_CLIENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Мои клиенты"]')
    MENU_ADD = (By.XPATH, '//android.widget.TextView[@content-desc="Добавить"]')
    MENU_MY_APPLICATIONS = (By.XPATH, '//android.widget.TextView[@content-desc="Мои заявки"]')
    MENU_MY_APPLICATIONS_REFINEMENT = (By.XPATH, '//android.widget.TextView[@content-desc="Доработка"]')
    MENU_ONLINE_APPLICATIONS = (By.XPATH, '//android.widget.TextView[@content-desc="Онлайн заявки"]')
    MENU_ONLINE_APPLICATIONS_INCOMING_APPLICATIONS = (By.XPATH, '//android.view.View[@content-desc="Входящие заявки"]')
    MENU_DETOP_MONITOR = (By.XPATH, '//android.widget.TextView[@content-desc="Монитор должников"]')
    MENU_MY_REPORTS = (By.XPATH, '//android.widget.TextView[@content-desc="Мои отчеты"]')
    MENU_MY_REPORTS_PAID_TODAY = (By.XPATH, '//android.widget.TextView[@content-desc="Оплатили сегодня"]')
    MENU_MY_REPORTS_PAID_BIRTHDAYS = (By.XPATH, '//android.widget.TextView[@content-desc="Дни рождения"]')
    MENU_MY_REPORTS_PAID_BIRTHDAYS_ACTIV = (By.XPATH, '//android.view.View[@content-desc="Активные"]')
    MENU_MY_REPORTS_PAID_PLANNED_REPAYMENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Планируемые погашения"]')
    MENU_MY_REPORTS_PAID_UNDELIVERED_ORIGINAL_ASP = (By.XPATH, '//android.widget.TextView[@content-desc="Несданные оригиналы АСП"]')
    MENU_MY_REPORTS_PAID_ISSUED_LOANS = (By.XPATH, '//android.widget.TextView[@content-desc="Выданные займы"]')
    MENU_MY_PERFOMANCE = (By.XPATH, '//android.widget.TextView[@content-desc="Мои показатели"]')
    MENU_MY_PERFOMANCE_CURRENTPERIOD = (By.XPATH, '//android.widget.TextView[@content-desc="Текущий период"]')
    MENU_LOAN_CALCULATOR = (By.XPATH, '//android.widget.TextView[@content-desc="Калькулятор займов"]')
    MENU_LOAN_CALCULATOR_DATE_OF_1_PAYMENT = (By.XPATH, '//android.view.View[@content-desc="Дата 1 платежа"]')
    MENU_SETTINGS = (By.XPATH, '//android.widget.TextView[@content-desc="Настройки"]')
    MENU_SETTINGS_ALLOW_LINE_SWIPE = (By.XPATH, '//android.widget.TextView[@content-desc="Разрешить смахивание строки"]')
    MENU_PAID_TODAY = (By.XPATH, '//android.widget.TextView[@content-desc="Оплатили сегодня "]')
    PAGE_CREATION_CLIENT = (By.XPATH, '//android.widget.TextView[@content-desc="Создание клиента"]')
    PAGE_ONLINE_APPLICATIONS = (By.XPATH, '//android.widget.TextView[@content-desc="Онлайн-заявки"]')
    BUTTON_BACK = (By.XPATH, '//android.view.View[@content-desc="Назад"]')
    BUTTON_CLOSE = (By.XPATH, '//android.widget.TextView[@content-desc="Закрыть"]')
    TOTAL_CLIENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Всего"]')
    # ABOUT_PROGRAM = (By.XPATH, '//android.widget.TextView[@content-desc="О программе"]')
    BASE = (By.XPATH, '//android.widget.TextView[@content-desc="База данных"]')
    TB_BAIBOL_DEMO = (By.XPATH, '//android.widget.TextView[@content-desc="tb_baibol_demo"]')
    TB_BAIBOL_K15 = (By.XPATH, '//android.widget.TextView[@content-desc="TBB-k15"]')
    TB_BAIBOL = (By.XPATH, '//android.widget.TextView[@content-desc="tb_baibol"]')
    LATEST_EVENTS_TEXT = (By.XPATH, '//android.widget.TextView[@content-desc="Последние события"]')
    TOTAL = (By.XPATH, '//android.widget.TextView[@content-desc="Итого"]')

    # Включение уведомлений
    BUTTON_CLEAR = (By.XPATH, '//android.view.View[@content-desc="Кнопка понятно"]')
    SWITH_NOTIFICATIONS = (By.ID, 'android:id/switch_widget')

    #  Прокрутка
    SCROLL_PUSH_NOTIFICATIONS = {'x_start': 450, 'y_start': 250,
                                 'x_finish': 450, 'y_finish': 100,
                                 'name_side': 'SCROLL_PUSH_NOTIFICATIONS', 'starting_point': 500}
    SCROLL_DOWN = {'x_start': 500, 'y_start': 1000,
                   'x_finish': 500, 'y_finish': 600,
                   'name_side': 'SCROLL_DOWN', 'starting_point': 1000}
    SCROLL_RIGHT_MENU_CLIENT_CARD = {'x_start': 800, 'y_start': 280,
                                     'x_finish': 50, 'y_finish': 280,
                                     'name_side': 'SCROLL_RIGHT_MENU_CLIENT_CARD', 'starting_point': 270}
    SCROLL_RIGHT_OTHER_DOC_PHOTO_DOCUMENTS = {'x_start': 600, 'y_start': 570,
                                              'x_finish': 250, 'y_finish': 570,
                                              'name_side': 'SCROLL_RIGHT_OTHER_DOC_PHOTO_DOCUMENTS', 'starting_point': 270}

    # Мои заявки
    MY_APPLICATIONS_FIO_CLIENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Поля. Мои заявки: ФИО клиента"]')

    # Поиск всех клиентов в карточке клиента
    FIO_CLIENT_ALL_CLIENTS = (By.XPATH, '//android.widget.TextView[@content-desc="ФИО"]')

    # Вкладки в карточке клиента переход через верхнее меню
    MENU_GENERAL_INFORMATIO = (By.XPATH, '//android.view.View[@content-desc="Значок Общее"]')
    MENU_DOCUMENTS = (By.XPATH, '//android.view.View[@content-desc="Значок Документы"]')
    MENU_WORK_AND_INCOME = (By.XPATH, '//android.view.View[@content-desc="Значок ДоходыРасходы"]')
    MENU_CONTACT_PERSONS = (By.XPATH, '//android.view.View[@content-desc="Значок Контакты"]')
    MENU_INN_SNILS = (By.XPATH, '//android.view.View[@content-desc="Значок ИННСНИЛС"]')
    MENU_OTHER_DOCUMENTS = (By.XPATH, '//android.view.View[@content-desc="Значок ДругиеДокументы"]')
    MENU_ASP = (By.XPATH, '//android.view.View[@content-desc="Значок АСП"]')
    MENU_APPLICATIONS_AND_CONTRACTS = (By.XPATH, '//android.view.View[@content-desc="Значок Заявки"]')
    MENU_VESIT_INSPECTIONS = (By.XPATH, '//android.view.View[@content-desc="Значок Визиты"]')
    MENU_PROPERTY = (By.XPATH, '//android.view.View[@content-desc="Значок Имущество"]')

    # Для нескольких или всех страниц карточки клиента
    BUTTON_SAVE = (By.XPATH, '//android.view.View[@content-desc="Сохранить"]')
    SAVE_CLOSE_CLIENT_CARD = (By.XPATH, '//android.widget.TextView[@content-desc="Закрыть/Сохранить"]')
    BUTTON_NEXT = (By.XPATH, '//android.view.View[@content-desc="Далее"]')
    BUTTON_ADD_PHOTOS = (By.XPATH, '//android.view.View[@content-desc="Кнопка добавить фото"]/..')
    SWITCH = (By.XPATH, '//android.view.View[@content-desc="Переключатель"]')
    MAKE_PHOTO = (By.XPATH, '//android.view.View[@content-desc="Кнопка сделать снимок"]/..')
    SELECT_PHOTO_FROM_DEVICES = (By.XPATH, '//android.view.View[@content-desc="Кнопка выбрать с устройства"]/..')
    CAMERA_PERMISSION_BUTTON = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    PHOTO_IN_GALLERY = (By.ID, 'com.google.android.documentsui:id/icon_thumb')
    PHOTO_GEOPOZITION = 4
    CANCEL_BUTTUN = (By.XPATH, '//android.view.View[@content-desc="Кнопка Отмена"]')
    JUMP_UP = (By.XPATH, '//android.widget.ImageButton[@content-desc="Перейти вверх"]')
    PHOHO_ALL_GALLERY_OLD = (By.ID, 'com.google.android.documentsui:id/thumbnail')
    PHOHO_ALL_GALLERY = (By.ID, 'com.google.android.providers.media.module:id/icon_thumbnail')

    # ФИО Клиента созданного customer_search_all_fields
    TEXT_FOR_SEARCH_NEW_CLIENT = "тестфамилия тестимя тестотчество"
    TEXT_FOR_SEARCH_NEW_CLIENT_RES = "Тестфамилия Тестимя Тестотчество"

    # ФИО существующего клиента, для проверки изменения полей сохранения карточки, дата рождения и номер телефона
    TEXT_FOR_SEARCH_OLD_CLIENT = "тестфамилия изменение существующего"
    TEXT_FOR_SEARCH_OLD_CLIENT_RES = "Тестфамилия Изменение Существующего"
    DATE_OF_BIRTHDAY_OLD_CLIENT_TEXT = '01.01.2000'
    PHONE_NUMBER_OLD_CLIENT_TEXT = '79310000007'


    # ФИО Добавления новой заявки на займ
    TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN = 'тестфамилия заявка тестотчество'
    TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN_RES = 'Тестфамилия Заявка Тестотчество'

    # ФИО Добавления новой заявки на займ на ДЕМО
    TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN_DEMO = 'ааааааа иван михайлович'
    TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN_RES_DEMO = 'Ааааааа Иван Михайлович'

    # ФИО Для проврки ТС ДЕМО
    TEXT_FOR_SEARCH_CLIENT_PROPERTY_DEMO = 'аспемова ивана михайловна'
    TEXT_FOR_SEARCH_CLIENT_PROPERTY_RES_DEMO = 'Аспемова Ивана Михайловна'

    #Поиск клиента в "Мои клиенты"
    MY_CLIENTS_MENU_ALL = (By.XPATH, '//android.widget.TextView[@content-desc="Все"]')
    EDIT_TEXT_SEARH_CLIENT = (By.XPATH, '//android.view.View[@content-desc="Поле Поиск по ФИО или телефону"]/../..')


    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger

    @allure.step
    def open_old_client(self, search_text, res_searc_text, search_accurate=True):
        """Функция для открытия клиента, вызывается сразу после открытия базы,
        на вход подается ФИО в нижнем ригистре и ФИО с заглавной.
        (сделано для выбора элемента из списка с Заглавными, чтобы не брать 2й элемент)"""
        self.click_element(self.MENU_MY_CLIENTS)
        self.click_element(self.MY_CLIENTS_MENU_ALL)
        element_edit_text_searc_client = self.search_element(self.EDIT_TEXT_SEARH_CLIENT)
        element_edit_text_searc_client.send_keys(search_text)
        element_fio_client = self.search_all_elements(self.FIO_CLIENT_ALL_CLIENTS)
        try:
            if search_accurate:
                assert element_fio_client[0].text == res_searc_text
        except AssertionError:
            self.logger.error(f"open_old_client AssertionError {element_fio_client[0].text} != {res_searc_text}")
            self.error_save_screenshot()
            raise NoSuchElementException(f"open_old_client AssertionError {element_fio_client[0].text} != {res_searc_text}")
        try:
            element_fio_client[0].click()
        except Exception:
            self.logger.error(
                f"open_old_client сработало исключние принажатии на первый элемент из спика клиентов element_fio_client[0].click()")
            self.error_save_screenshot()
        try:
            assert self.field_presence_check(self.CLIENT_CARD_SURNAME, wait_time=20)
        except AssertionError:
            self.logger.error(f"open_old_client сработал assert self.field_presence_check, в поле не вставлено значение {self.CLIENT_CARD_SURNAME}")
            self.error_save_screenshot()

    @allure.step
    def select_field_value(self, field, field_list):
        """Перебор всех значений. Проверка полей с выбором, на вход подается селектор поля,
        для нажатия после выбора и список значений прлей, пеербираем все значения и проверяем,
         что поле выбралось. Идет подсчет значений
        и при выборе последнего значения на поле нажатие не происходит"""
        element_fild_len = 0
        for element_field in field_list:
            selector = (By.XPATH, f'//android.widget.TextView[@content-desc="{element_field}"]')
            self.click_element(selector)
            element = self.check_text_by_selector(field)
            assert element == element_field
            element_fild_len += 1
            if element_fild_len != len(field_list):
                self.click_element(field)


    def celect_name_menu(self, element_menu):
        menu_dict = {'Последние события': self.MENU_LATEST_EVENTS, 'Мои клиенты': self.MENU_MY_CLIENTS,
                     'Последние события текст': self.LATEST_EVENTS_TEXT,
                     'Добавить': self.MENU_ADD, 'Мои заявки': self.MENU_MY_APPLICATIONS,
                     'Онлайн заявки': self.MENU_ONLINE_APPLICATIONS, 'Монитор должников': self.MENU_DETOP_MONITOR,
                     'Мои отчеты': self.MENU_MY_REPORTS, 'Мои показатели': self.MENU_MY_PERFOMANCE,
                     'Калькулятор займов': self.MENU_LOAN_CALCULATOR, 'Настройки': self.MENU_SETTINGS,
                     'Оплатили сегодня ': self.MENU_PAID_TODAY, 'Поиск клиента': self.PAGE_CREATION_CLIENT,
                     'Онлайн-заявки': self.PAGE_ONLINE_APPLICATIONS}
        return menu_dict[element_menu]

    # @allure.step
    # def login_km(self, base, km_password):
    #     """Открывает страницу поиск клиента, указать селектор базы"""
    #     self.base_change(base)
    #     time.sleep(0.1)
    #     self.sig_in(km_password)

    def error_save_screenshot(self):
        """Делает фото экрана, втавляем в исключения"""
        self.driver.save_screenshot(f"logs/sech_element_{datetime.datetime.now()}.png")
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=f"sech_element_{datetime.datetime.now()}",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step
    def sig_in(self, km_password):
        """Ввод пароля из PASSWORD, необходимо указывать локаторы цифр"""
        time.sleep(0.3)
        for selector in km_password:
            try:
                self.logger.info(f"sig_in selector = {selector}")
                wait = WebDriverWait(self.driver, 6)
                element = wait.until(EC.presence_of_element_located(selector))
                element.click()
            except NoSuchElementException:
                self.logger.error(f"sig_in no serch element {selector} ")
                self.error_save_screenshot()
                raise NoSuchElementException(f"sig_in no serch element {selector} ")
        if self.field_presence_check(self.FINGERPRINT_TEXT_FIELD):
            self.click_element(self.FINGERPRINT_NO)
        # for i in range (4):
        #     try:
        #         # self.driver.find_element(by=AppiumBy.XPATH, value=self.PASSWORD[i]).click()
        #         selector = (By.XPATH, self.PASSWORD[i])
        #         self.logger.info(f"sig_in selector = {selector}")
        #         wait = WebDriverWait(self.driver, 6)
        #         element = wait.until(EC.presence_of_element_located(selector))
        #         element.click()
        #     except NoSuchElementException:
        #         self.logger.error(f"sig_in no serch element {self.PASSWORD[i]} ")
        #         self.error_save_screenshot()
        #         raise NoSuchElementException(f"sig_in no serch element {self.PASSWORD[i]} ")

    @allure.step
    def click_element(self, selector, wait_time=6):
        """Нажатие на элемент, принимает селектор для нажатия,
        возвращает элемент"""
        try:
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.element_to_be_clickable(selector))
            element.click()
            time.sleep(0.2)
            self.logger.info(f"click_element Нажали на элемент с селектором {selector}")
            return element
        except Exception as e:
            self.logger.error(f"e = {e}")
            self.logger.error(f"Exception click_element  selector = {selector}")
            self.error_save_screenshot()
            raise AssertionError(f"Exception click_element  selector = {selector}")

    @allure.step
    def scrolls_all(self, scrol_name, scroll_page_selector=False, selector_scroll_to_element=False):
        """Прокрутка, принимает какую прокрутку будет делать, также
        принимает селектор страницы (элемента) с которого будет начинаться прокрутка
        (сделано чтобы сделать паузу перед прокруткой) и
        селектор элемента до которого будет прокрутка"""
        flag = 0
        if scroll_page_selector:
            self.logger.info(f"scrolls_all открыта страница 'Общая информация', scrol_name = {scrol_name}, "
                             f"scroll_page_selector = {scroll_page_selector}")
            try:
                assert self.field_presence_check(scroll_page_selector, wait_time=10)
            except AssertionError:
                self.logger.error(f"scrolls_all нет селектора scroll_page_selector = {scroll_page_selector}")
                self.error_save_screenshot()
        while flag < 8:
            chain = ActionChains(self.driver, duration=scrol_name['starting_point'])
            input = chain.w3c_actions.add_pointer_input(interaction.POINTER_TOUCH, "finger1")
            input.create_pointer_move(x=scrol_name['x_start'], y=scrol_name['y_start'])
            input.create_pointer_down(button=MouseButton.LEFT)
            input.create_pointer_move(x=scrol_name['x_finish'], y=scrol_name['y_finish'])
            input.create_pointer_up(button=MouseButton.LEFT)
            chain.perform()
            time.sleep(0.1)
            self.logger.info(f"scrolls_all Сделана прокрутка экрана {scrol_name['name_side']} на "
                             f"x_start = {scrol_name['x_start']} y_start = {scrol_name['y_start']}, "
                             f"x_finish = {scrol_name['x_finish']} y_finish = {scrol_name['y_finish']}")
            if selector_scroll_to_element:
                flag += 1
                if self.field_presence_check(selector_scroll_to_element, wait_time=1):
                    return True
            else:
                return True

    def main_menu(self):
        """Проверка наличия всех меню из списка MAIN_MENU, с прокруткой для отображения нижних пунктов меню"""
        textview = self.text_view()
        for name_menu in self.ALL_TEXT_VIEW:
            if name_menu in textview:
                self.logger.info(f"main_menu Ищем меню {name_menu}")
            else:
                self.scrolls_all(self.SCROLL_DOWN)
                textview = self.text_view()
                self.logger.info(f"main_menu Ищем меню, если не поместилось на экран {textview}")
                if name_menu in textview:
                    return True
                else:
                    self.logger.error(f"main_menu нет в меню: {name_menu}")
                    assert False

    def text_view(self):
        """Получение всех текстовых полей на странице, только тех, что видно на странице, записываем их в список"""
        element_textview_text = []
        try:
            textview = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.TextView")
        except NoSuchElementException:
            self.logger.error(f"text_view не найден элементы 'android.widget.TextView' ")
            raise AssertionError(f"text_view не найден элементы 'android.widget.TextView' ")
        for el_textview in textview:
            element_textview_text.append(el_textview.text)
        self.logger.info(f"text_view все текстовые поля на странице: {element_textview_text}")
        return element_textview_text


    def open_menu(self, element_menu):
        selector = self.celect_name_menu(element_menu)
        element = self.click_element(selector)
        return element

    @allure.step
    def check_text(self, text):
        """Для меню на главной странице.
        Получить текст по тексту, ключу из celect_name_menu"""
        try:
            selector = self.celect_name_menu(text)
            wait = WebDriverWait(self.driver, 5)
            header_main_page = wait.until(EC.presence_of_element_located(selector))
            # time.sleep(1)
            self.logger.info(f"check_text header_main_page.text = {header_main_page.text}")
            text_pages = header_main_page.text
            return text_pages
        except Exception as e:
            self.logger.error(f"check_text except e = {e} ")
            self.logger.error(f"check_text selector = {selector}")
            self.error_save_screenshot()
            raise AssertionError(f"check_text selector = {selector}")

    @allure.step
    def check_text_by_selector(self, selector):
        """Получить текст по селектору"""
        try:
            wait = WebDriverWait(self.driver, 20)
            text_field = wait.until(EC.presence_of_element_located(selector))
            self.logger.info(f"check_text_by_selector selector = {selector}")
            self.logger.info(f"check_text_by_selector  = {text_field.text}")
            text_in_field = text_field.text
            return text_in_field
        except Exception as e:
            self.logger.error(f"check_text_by_selector except e = {e} ")
            self.logger.error(f"check_text_by_selector selector = {selector}")
            self.error_save_screenshot()
            raise AssertionError

    @allure.step
    def button_click(self, selector):
        wait = WebDriverWait(self.driver, 4)
        try:
            element = wait.until(EC.visibility_of_element_located(selector))
            element.click()
            self.logger.info(f"button_click Нажали на кнопку с селектором {selector}")
        except TimeoutException:
            self.logger.error(f"button_click Не Дождался элемента с селектором {selector}")
            raise AssertionError(f"button_click Не Дождался элемента с селектором {selector}")

    # @allure.step
    # def base_change(self, selector):
    #     self.click_element(self.ABOUT_PROGRAM)
    #     self.click_element(self.BASE)
    #     self.logger.info(f"BASE selector = {selector}")
    #     self.click_element(selector)
    #     # assert self.field_presence_check(self.PASSWORD_ONE, wait_time=20)

    @allure.step
    def search_element(self, selector):
        """Выбор элемента, принимает селектор, возвращает элемент"""
        try:
            wait = WebDriverWait(self.driver, 4)
            element = wait.until(EC.presence_of_element_located(selector))
            self.logger.info(f"search_element выбран элемент с селектором {selector}")
            # element = self.driver.find_element(by=AppiumBy.XPATH, value=selector) # Поиск по селектору Appium
            return element
        except TimeoutException:
            self.logger.error(f"search_element Нет на странице элемента с селектором {selector}")
            self.error_save_screenshot()
            raise AssertionError(f"search_element Нет на странице элемента с селектором {selector}")

    @allure.step
    def search_addresses(self, selector, element, text_in_field):
        """Поиск адресов, в строку поиска вставляем адрес и проверяем появился список или нет.
        Предаем селектор, объектт поля для вставки текста и текст,
        если список не появился делаем паузу и вставляем текст еще раз"""
        amount = 0
        while amount != 4:
            try:
                element.send_keys(text_in_field)
                wait = WebDriverWait(self.driver, 4)
                element = wait.until(EC.presence_of_all_elements_located(selector))
                self.logger.info(f"search_all_elements выбраны все элементы с селектором {selector}")
                # element = self.driver.find_element(by=AppiumBy.XPATH, value=selector) # Поиск по селектору Appium
                return element
            except TimeoutException:
                amount += 1
                time.sleep(1)
                self.logger.error(f"search_all_elements, количество проходов цикла {amount}. Нет на странице элементов с селектором {selector}")
                self.error_save_screenshot()
                if amount == 4:
                    raise AssertionError(f"search_all_elements, количество проходов цикла {amount}. Нет на странице элементов с селектором {selector}")

    @allure.step
    def search_all_elements(self, selector):
        """Возвращает объект содержащий все элементы с селектором"""
        try:
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(EC.presence_of_all_elements_located(selector))
            self.logger.info(f"search_all_elements выбраны все элементы с селектором {selector}")
            return elements
        except TimeoutException:
            self.logger.error(
                f"search_all_elements. Нет на странице элементов с селектором {selector}")
            self.error_save_screenshot()
            raise AssertionError(
                f"search_all_elements. Нет на странице элементов с селектором {selector}")

    @allure.step
    def search_text_in_elements(self, elements, text_search):
        """Для перебора элементов, на вход, список элементов и текст, для сравнения,
        если находит совпадение assert True, в противном случае False,
        ничего не возвращяет"""
        text_list = []
        for text in elements:
            text_list.append(text.text)
        if text_search in text_list:
            assert True
        else:
            assert False

    @allure.step
    def change_field_with_select(self, selector_field, field_list):
        """Изменение полей с выбором, на вход подается селектор поля,
        для нажатия после выбора и список значений прлей. Проверяется текущее значение и
        из списка выбирается отличное значени, заполняется поле проверяется, что поле принято новое значение,
        возвращает список ['Вид на жительство', ('//android.widget.TextView[@content-desc="Тип дополнительного документа:"]')]"""
        self.logger.info(f"change_field_with_select переданы selector_field = {selector_field} и "
                         f"field_list = {field_list}")
        try:
            value_field = self.check_text_by_selector(selector_field)
            self.logger.info(f"change_field_with_select value_field = {value_field}")
            self.click_element(selector_field)
            counter = 0
            for element_field in field_list[1:]:
                counter += 1
                if element_field != value_field:
                    selector = (By.XPATH, f'//android.widget.TextView[@content-desc="{element_field}"]')
                    if self.field_presence_check(selector):
                        self.click_element(selector)
                        new_value_field = self.check_text_by_selector(selector_field)
                        assert element_field == new_value_field
                        value_list = [element_field, selector_field]
                        return value_list
            selector = (By.XPATH, f'//android.widget.TextView[@content-desc="{field_list[counter]}"]')
            self.click_element(selector)
            value_list = [field_list[counter], selector_field]
            return value_list
        except Exception:
            self.error_save_screenshot()
            self.logger.error(f"Возникла ошибка в change_field_with_select, field = {selector_field},"
                              f" field_list = {field_list}")
            raise AssertionError(f"Возникла ошибка в change_field_with_select, field = {selector_field},"
                              f" field_list = {field_list}")

    @allure.step
    def compare_text_in_field(self, selector_field, text, phone=False, date=False, wait_time=6):
        """Проверка что текст в поле и который передали, одинаковый.
        Получает селектор поля и текст.
        Если проверяется поле с номером телефона необходимо передавать phone=True
        Еси поле с датой необходимо передать date=True"""
        try:
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.presence_of_element_located(selector_field))
            text_element = element.text
            if phone:
                text_element = self.editing_phone_number(text_element)
                text = self.editing_phone_number(text)
            if date:
                text_element = self.editing_date(text_element)
                text = self.editing_date(text)

            self.logger.info(f"compare_text_in_field выбраны все элементы с селектором {selector_field}")
            self.logger.info(f"текст был в поле text_element = {text_element}, текст должен быть в поле {text}")
            try:
                assert text_element == text
            except AssertionError:
                self.logger.error(f"compare_text_in_field сработал assert значение в поле '{text_element}', "
                                 f"значение вводимого текста '{text}'."
                                  f"селектор {selector_field}")
                self.error_save_screenshot()
                raise AssertionError(f"compare_text_in_field сработал assert значение в поле '{text_element}', "
                                 f"значение вводимого текста '{text}'"
                                     f"селектор {selector_field}")
        except TimeoutException:
            self.logger.error(f"compare_text_in_field Нет на странице элементов с селектором {selector_field}")
            self.error_save_screenshot()
            raise AssertionError(f"compare_text_in_field Нет на странице элементов с селектором {selector_field}")

    @allure.step
    def field_presence_check(self, selector, wait_time=4):
        """Проверка наличия поля, если есть возвращает True, если нет False"""
        try:
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.presence_of_element_located(selector))
            self.logger.info(f"field_presence_check, Проверка наличия элемента, выбран элемент с селектором {selector}")
            return True
        except TimeoutException:
            self.logger.info(f"field_presence_check, Проверка наличия элемента, Нет на странице элемента с селектором {selector}")
            return False # Тут боязательно надо False, его ждут, исключение используется для проверки

    def random_all(self, series=False, nuber=False,
                   str_latin=False, str_cyrillic=False,
                   date=False, date_end=False,day=False,
                   phone=False, patronymic=False, len_srt=2):
        """Генерирует значения для заполения полей.
        По умолчанию length=2, series=False, nuber=False,
        str_latin=False, str_cyrillic=False,
        date=False, date_end=False,day=False"""
        letters = ""
        if series:
            letters = 'QWERTYASDFGZXCVB'
        elif nuber:
            letters = '1234567890'
        elif str_latin:
            letters = 'qwjfbfobnwlmefwlpmfwnveofvneweqwc'
        elif str_cyrillic or patronymic:
            letters = 'ЕпОоЫВаДнБлАлХхРрСсМмИиТтЬьБбЮюЯяЧч'
        elif date or date_end or day:
            letters = '123456789'
        elif phone:
            len_srt = 10
            letters = '1234567890'
        random_str = ''.join(random.choice(letters) for i in range(len_srt))
        if nuber:
            while random_str[0] == '0':
                random_str = random_str[1:] + '0'
        if patronymic:
            return "Тестотчество" + random_str
        if phone:
            return "7" + random_str
        if date or date_end or day:
            while int(random_str) > 31:
                random_str = ''.join(random.choice(letters) for i in range(len_srt))
            if date:
                random_date = random_str + '.02.2023'
                return random_date
            if date_end:
                random_date_end = random_str + '.01.2033'
                return random_date_end
            else:
                return random_str
        return random_str

    # def random_str(self):
    #     length = 5
    #     letters = 'qwjfbfobnwlmefwlpmfwnveofvneweqwc'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str

    # def random_cyrillic_str(self):
    #     length = 15
    #     letters = 'ЕпОоЫВаДнБлАл'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str

    # def random_numeric_value(self, length=5):
    #     letters = '123456789'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str

    # def random_date_month(self):
    #     length = 2
    #     letters = '123456789'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     while int(random_str) > 31:
    #         random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str

    # def random_phone_number(self):
    #     length = 10
    #     letters = '1234567890'
    #     random_str_phone_nubber = ''.join(random.choice(letters) for i in range(length))
    #     return "7" + random_str_phone_nubber

    # def random_patronymic_str(self):
    #     length = 7
    #     letters = 'ЕпОоЫВаДнБлАлХхРрСсМмИиТтЬьБбЮюЯяЧч'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return "Тестотчество" + random_str

    # def random_series_doc(self, length=2):
    #     letters = 'QWERTYASDFGZXCVB'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str

    # def random_series_doc_rf(self):
    #     length = 4
    #     letters = '1234567890'
    #     random_str = ''.join(random.choice(letters) for i in range(length))
    #     return random_str



    @allure.step
    def checking_field_values_from_list(self, value_list):
        """Проверка заполнения полей верными данными,
        на вход список списков, первый элемент селектор поля с текстом, второй значение которое должно быть в поле
        если поля нет, делается прокрутка вниз на 3 пункта"""
        for element_list in value_list:
            if self.field_presence_check(element_list[1]):
                pass
            else:
                self.scrolls_all(self.SCROLL_DOWN)
                self.scrolls_all(self.SCROLL_DOWN)
                self.scrolls_all(self.SCROLL_DOWN)
            text_field = self.check_text_by_selector(element_list[1])
            try:
                assert text_field == element_list[0]
            except AssertionError:
                self.logger.error(f"Возникла ошибка в checking_field_values_from_list, value_list = {value_list},"
                                  f"text_field = {text_field}, element_list[0] = {element_list[0]}")
                self.error_save_screenshot()
                assert False

    @allure.step
    def find_text_on_page(self, selector, serch_text):
        """Найти текст на странице, если текста нет, делам прокрутку пока не увидим кнопку Далее
        Если текста нет и есть кнопка Далее, вызывается NoSuchElementException.
        Элемент с текстом {serch_text} не найден"""
        flag = True
        while flag:
            elements = self.search_all_elements(selector)
            counter = 0
            for element in elements:
                text_element = element.text
                self.logger.info(f"При перебирании элементов выбран элемент {text_element} сравниваем с {serch_text}")
                if text_element == serch_text:
                    self.logger.info(f"Выбранные элементы равны {text_element} = {serch_text},"
                                     f"номер эемента по счету {counter}")
                    return counter
                counter += 1
            self.scrolls_all(self.SCROLL_DOWN)
            element_button_next = self.field_presence_check(self.BUTTON_NEXT)
            if element_button_next:
                flag = False
                self.logger.error(f"Элемент с текстом {serch_text} не найден")
                raise NoSuchElementException(f"Элемент с текстом {serch_text} не найден")

    def editing_phone_number(self, number_phone):
        """Для номера телефона, убирает лишние символы, оставляя только номер из цифр без пробелов и лишних знаков"""
        new_number_phone = number_phone.replace(" ", "").replace("-", "").replace("+", "").replace("(", "").replace(")", "")
        return new_number_phone

    def editing_date(self, text_date):
        """Для даты, убирает точки и пробелы"""
        new_text_date = text_date.replace(" ", "").replace(".", "")
        return new_text_date


    @allure.step
    def get_selector_by_text(self, text_field):
        """Выбрать из списка поле по названию,
        принимает название, возвращяет селектор"""
        try:
            wait = WebDriverWait(self.driver, 6)
            selector = (By.XPATH, f'//android.widget.TextView[@content-desc="{text_field}"]')
            self.logger.info(f"get_selector_by_text Выбрали поле {text_field}")
            self.logger.info(f"get_selector_by_text получили селектор {selector}")
            return selector
        except Exception as e:
            self.logger.error(f"e = {e}")
            self.logger.error(f"get_selector_by_text  text_field = {text_field}")
            self.error_save_screenshot()
            raise AssertionError(f"get_selector_by_text  text_field = {text_field}")

    @allure.step
    def search_text_in_page(self, text):
        """Поиск текста на странице, если текст есть, то возвращает True"""
        elements = self.text_view()
        self.logger.info(f"search_text_in_page elements = {elements}")
        for element in elements:
            if element == text:
                return True
        return False

    @allure.step
    def clear_and_send_keys(self, selector, text, phone=False, date=False, compare_text_in_field=True):
        """Очищает поле и вставляет текст,
        принимает селектор для поиска элемента и текст для вставки"""
        element = self.search_element(selector)
        element.click()
        self.driver.hide_keyboard()
        element.clear()
        self.logger.info(f"clear_and_send_keys в поле с селектором {selector}, вставлен текст = '{text}'")
        time.sleep(0.5)
        try:
            element.send_keys(text)
            self.driver.hide_keyboard()
        except Exception:
            self.logger.error(f"clear_and_send_keys текст не вставился send_keys, selector = {selector}, text = {text}")
            self.error_save_screenshot()
            raise Exception(f"clear_and_send_keys текст не вставился send_keys, selector = {selector}, text = {text}")
        if compare_text_in_field:
            self.compare_text_in_field(selector, text, phone=phone, date=date)

    def find_search_field_two_scrolls(self, selector):
        """Принимает селектор поля, делает 2 прокрутки и
         провкеряет наличие поля если оно есть, True"""
        self.scrolls_all(self.SCROLL_DOWN)
        self.scrolls_all(self.SCROLL_DOWN)
        return self.field_presence_check(selector)

    def positive_assert_validation_field_location(self, selector_validation, selector_field, text, wait_time=1):
        """Для позитивной проверки поля. Проверка появления поля валидации, при верном заполнении поля.
        На входе селектор поля валидации, селектор поля с текстом, сам текст, время выполнения (не обязательный параметр).
        Если поле заполнено верно, поле валидации не появится и в ответе получаем True, в противном случае получаем AssertionError"""
        try:
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(EC.presence_of_element_located(selector_validation))
            self.logger.error(f"assert_validation_field_location отображается поле вылидации = {selector_validation}"
                             f"\n поле для валидации  = {selector_field}, Текст вставленный в поле {text}")
            self.error_save_screenshot()
            raise AssertionError(f"assert_validation_field_location отображается поле вылидации = {selector_validation}"
                             f"\n поле для валидации  = {selector_field}, Текст вставленный в поле {text}")
        except TimeoutException:
            self.logger.info(f"assert_validation_field_location, Поле проверки не отобраается, селектор поля валидации {selector_validation}"
                             f"\n селектор поля с текстом {selector_field}")
            return True

    def negetive_assert_validation_field_location(self, selector_validation, selector_field, text, type_testing='positiv', wait_time=1):
        """Для негативной проверки поля. Проверка появления поля валидации, при неверном заполнении поля.
        На входе селектор поля валидации, селектор поля с текстом, сам текст, время выполнения (не обязательный параметр).
        Если поле заполнено неверно, появляется поле валидации и в ответе получаем True, в противном случае получаем AssertionError"""
        try:
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(EC.presence_of_element_located(selector_validation))
            self.logger.info(f"assert_validation_field_location, Поле проверки не отобраается, селектор поля валидации {selector_validation}"
                             f"\n селектор поля с текстом {selector_field}")
            return True
        except TimeoutException:
            self.logger.error(f"assert_validation_field_location отображается поле вылидации = {selector_validation}"
                              f"\n поле для валидации  = {selector_field}, Текст вставленный в поле {text}")
            self.error_save_screenshot()
            raise AssertionError(f"assert_validation_field_location отображается поле вылидации = {selector_validation}"
                                 f"\n поле для валидации  = {selector_field}, Текст вставленный в поле {text}")


    def validations_field(self, selector_field, selector_validation_field, list_validations,
                          validation="positive", phone=False, date=False):
        """Метод для проверки полей на валидацию, подставляет значения мз листа list_validations в поле.
        Может проверять, как позитавные, так и негативные входные данные.
        На вход подается селектор поля котрое проверяем, селектор поля валидации (которое появляется),
        list значений, которые будут подставлены в поле и validation, который определяет позитивный или негативный тест"""
        for text_validation in list_validations:
            if validation == "positive":
                self.clear_and_send_keys(selector_field, text_validation, phone=phone, date=date)
                self.positive_assert_validation_field_location(selector_validation_field, selector_field, text_validation)
            else:
                self.clear_and_send_keys(selector_field, text_validation, compare_text_in_field=False)
                self.negetive_assert_validation_field_location(selector_validation_field, selector_field, text_validation)

