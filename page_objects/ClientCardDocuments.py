import random
from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardDocuments(MainPage):

    # Документы Селекторы
    HEADING_DOCUMENTS = (By.XPATH, '//android.widget.TextView[@content-desc="Документы"]')
    CLIENT_CARD_DOC_TYPE_MAIN_DOC = (By.XPATH, '//android.widget.TextView[@content-desc="Тип основного документа:"]')
    NUNBER_DOC = (By.XPATH, '//android.view.View[@content-desc="Номер документа"]/..')
    NUNBER_DOC_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Номер документа валидация"]')
    DOC_ISSUED_BY = (By.XPATH, '//android.view.View[@content-desc="Кем выдан"]/..')
    DOC_ISSUED_BY_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Кем выдан валидация"]')
    DOC_DEPARTAMENT_CODE = (By.XPATH, '//android.view.View[@content-desc="Код подразделения"]/..')
    DOC_DEPARTAMENT_CODE_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Код подразделения валидация"]')
    CLIENT_CARD_DOC_DOC1_DATE = (By.XPATH, '//android.view.View[@content-desc="Дата выдачи основного документа:"]/..')
    CLIENT_CARD_DOC_DOC1_END_DATE = (By.XPATH, '//android.view.View[@content-desc="Срок действия основного документа:"]/..')
    CLIENT_CARD_DOC_PLACE_BIRTH = (By.XPATH, '//android.view.View[@content-desc="Место рождения"]/..')
    CLIENT_CARD_DOC_PLACE_BIRTH_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Место рождения валидация"]')
    CLIENT_CARD_DOC_ADDRESS_HOMELAND = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес регистрации проживания на родине"]')
    CLIENT_CARD_DOC_FACT_ADDRESS_HOMELAND = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес проживания на родине"]')
    CLIENT_CARD_DOC_TYPE_SECOND_DOC = (By.XPATH, '//android.widget.TextView[@content-desc="Тип дополнительного документа:"]')
    CLIENT_CARD_DOC_SERIES = (By.XPATH, '//android.view.View[@content-desc="Серия документа"]/..')
    CLIENT_CARD_DOC_SERIES_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Серия документа валидация"]')
    CLIENT_CARD_SECOND_DOC_DATE = (By.XPATH, '//android.view.View[@content-desc="Дата выдачи дополнительного документа:"]/..')
    CLIENT_CARD_SECOND_DOC_END_DATE = (By.XPATH, '//android.view.View[@content-desc="Срок действия дополнительного документа:"]/..')

    # Вкладка Документы заполение нового клиента
    CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT = (By.XPATH, '//android.widget.TextView[@content-desc="Паспорт иностранного гражданина"]')
    CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT_RF = (By.XPATH, '//android.widget.TextView[@content-desc="Паспорт гражданина РФ"]')
    DOC_SERIES_TEXT = 'RR'
    DOC_SERIES_TEXT_RF = '1234'
    DOC_NUNBER_DOC_TEXT = '111111'
    DOC_NUNBER_DOC_TEXT_RF = '123456'
    DEPARTAMENT_CODE_RF = '123123'
    DEPARTAMENT_CODE_RF_FIELD = '123-123'
    DOC_ISSUED_BY_TEXT = 'ISP TEST'
    DOC_ISSUED_BY_TEXT_RF = 'ОВД СПб'
    DOC1_DATE_TEXT = '01032022'
    DOC1_DATE_TEXT_IN_FIELD = '01.03.2022'
    DOC1_END_DATE_TEXT = '28022032'
    DOC1_END_DATE_TEXT_IN_FIELD = '28.02.2032'
    PLACE_BIRTH_TEXT = 'Место рождения'
    CLIENT_CARD_DOC_TYPE_SECOND_DOC_MIGR = (By.XPATH, '//android.widget.TextView[@content-desc="Миграционная карта"]')
    SECOND_DOC_SERIES_TEXT = 'SS'
    SECOND_DOC_NUMBER_TEXT = '22222'
    SECOND_DOC_ISSUED_BY_TEXT = 'SECOND ISP TEST'
    SECOND_DOC_DATE_TEXT = '02042022'
    SECOND_DOC_DATE_TEXT_IN_FIELD = '02.04.2022'
    SECOND_DOC_END_DATE_TEXT = '01032025'
    SECOND_DOC_END_DATE_TEXT_IN_FIELD = '01.03.2025'

    #Для быстрой подмены
    KYRGYZSTAN= 'КИРГИЗИЯ'
    RUSSIA = 'РОССИЯ'
    TAJIKISTAN = 'ТАДЖИКИСТАН'
    UZBEKISTAN = 'УЗБЕКИСТАН'

    # типы документов по странам
    TYPE_MAIN_DOC_KYRGYZSTAN = {'КИРГИЗИЯ': ['Не выбрано', 'ID карта', 'Паспорт иностранного гражданина']}
    TYPE_MAIN_DOC_RUSSIA = {'РОССИЯ': ['Не выбрано', 'Паспорт гражданина РФ']}
    TYPE_MAIN_DOC_TAJIKISTAN = {'ТАДЖИКИСТАН': ['Не выбрано', 'Паспорт иностранного гражданина']}
    TYPE_MAIN_DOC_UZBEKISTAN = {'УЗБЕКИСТАН': ['Не выбрано', 'Паспорт иностранного гражданина']}

    TYPE_SECOND_DOC_KYRGYZSTAN = {'КИРГИЗИЯ': ['Не выбрано', 'ID карта', 'Вид на жительство',
                                  'Водительское удостоверение национальное',
                                  'Водительское удостоверение РФ', 'Миграционная карта',
                                  'Паспорт иностранного гражданина',
                                  'Разрешение на временное пребывание', 'Другой документ']}
    TYPE_SECOND_DOC_TAJIKISTAN = {'ТАДЖИКИСТАН': ['Не выбрано', 'Вид на жительство',
                                  'Водительское удостоверение национальное',
                                  'Водительское удостоверение РФ', 'Миграционная карта',
                                  'Паспорт иностранного гражданина', 'Патент',
                                  'Разрешение на временное пребывание', 'Другой документ']}
    TYPE_SECOND_DOC_UZBEKISTAN = {'УЗБЕКИСТАН': ['Не выбрано', 'Вид на жительство',
                                  'Водительское удостоверение национальное',
                                  'Водительское удостоверение РФ', 'Заграничный паспорт',
                                  'Миграционная карта', 'Паспорт иностранного гражданина',
                                  'Патент', 'Разрешение на временное пребывание', 'Другой документ']}
    DOCUMENT_TYPS_KYRGYZSTAN = ['Паспорт все страницы', 'Паспорт - лицевой разворот', 'Скан паспорта 4 и 5 страницы',
                            'Скан паспорта дети', 'Паспорт - ЗАГС сведения о браке', 'Паспорт - печать РВП',
                                'Паспорт - прописка на Родине', 'Штамп о въезде в РФ', 'Штамп о выезде из страны пребывания',
                                'Фото с паспортом']
    DOCUMENT_TYPS_RUSSIA = ['Паспорт все страницы', 'Скан паспорта 2 и 3 страницы', 'Скан паспорта 4 и 5 страницы',
                            'Скан паспорта дети', 'Паспорт - ЗАГС сведения о браке',
                            'Паспорт гр.РФ 19 стр (ранее выданный паспорт)', 'Фото с паспортом']
    DOCUMENT_TYPS_TAJIKISTAN = ['Паспорт все страницы', 'Паспорт - лицевой разворот', 'Скан паспорта 4 и 5 страницы',
                            'Скан паспорта дети', 'Паспорт - ЗАГС сведения о браке', 'Паспорт - печать РВП',
                                'Паспорт - прописка на Родине', 'Штамп о въезде в РФ', 'Штамп о выезде из страны пребывания',
                                'Фото с паспортом']
    DOCUMENT_TYPS_UZBEKISTAN = ['Паспорт все страницы', 'Паспорт - лицевой разворот', 'Скан паспорта 4 и 5 страницы',
                            'Скан паспорта дети', 'Паспорт - ЗАГС сведения о браке', 'Паспорт - печать РВП',
                                'Паспорт - прописка на Родине', 'Штамп о въезде в РФ', 'Штамп о выезде из страны пребывания',
                                'Фото с паспортом']
    # PHOHO_ALL_GALLERY = (By.ID, 'com.google.android.documentsui:id/thumbnail')
    PHOTO_PASSPORT_KYRGYZSTAN = 0
    PHOTO_PASSPORT_RUSSIA = 1
    PHOTO_PASSPORT_TAJIKISTAN = 2
    PHOTO_PASSPORT_UZBEKISTAN = 3

    TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF = 'тестфамилия россия'
    TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES = 'Тестфамилия Pоссия'

    TEXT_FOR_SEARCH_CLIENT_PASSPORT_KYRGYZSTAN = 'тестфамилия киргизия'
    TEXT_FOR_SEARCH_CLIENT_PASSPORT_KYRGYZSTAN_RES = 'Тестфамилия Киргизия'

    TEXT_FOR_SEARCH_CLIENT_PASSPORT_TAJIKISTAN = 'тестфамилия таджикистан'
    TEXT_FOR_SEARCH_CLIENT_PASSPORT_TAJIKISTAN_RES = 'Тестфамилия Таджикистан'

    TEXT_FOR_SEARCH_CLIENT_PASSPORT_UZBEKISTAN = 'тестфамилия узбекистан'
    TEXT_FOR_SEARCH_CLIENT_PASSPORT_UZBEKISTAN_RES = 'Тестфамилия Узбекистан'

    # Данные по валидации полей
    # По полям паспорта РФ
    LIST_POSITIVE_SERIES_PASSPORT_RF = ['1234', '0987', '0000']
    LIST_NEGATIVE_SERIES_PASSPORT_RF = ['', ' ', '1', '0', '123', '12345', 'qwer', 'йцук',
                                        'q', 'asdfg', 'фывап', 'ЙЦУКЕ', 'QWERT', '.123', '!2#$', '@-+()/":;']

    LIST_POSITIVE_NUNBER_DOC_PASSPORT_RF = ['123456', '012345', '000000']
    LIST_NEGATIVE_NUNBER_DOC_PASSPORT_RF = ['', ' ', '1234567', 'qwe', 'йцуке', '1йцу', '1qwert', ]

    LIST_POSITIVE_DOC_ISSUED_BY_PASSPORT_RF = ['123456', 'йцукенгшщзхъ', 'йцуке фывап', 'qwerty', '@-+()/":;', "'"]
    LIST_NEGATIVE_DOC_ISSUED_BY_PASSPORT_RF = ['', 'qwe#123', '~$!&?']

    LIST_POSITIVE_DEPARTAMENT_CODE = ['123456', '098765', '000000']
    LIST_NEGATIVE_DEPARTAMENT_CODE = ['', ' ', '123-456', '1', '12', '12345', 'йцукенгшщзхъ', 'йцуке фывап', 'qwerty', '@-+()/":;', "'"]

    LIST_POSITIVE_PLACE_BIRTH = ['qwer', 'q', 'йцуке', 'йцукенг фывапр', 'ЙЦУКЕ', 'QWERT', '123456']
    LIST_NEGATIVE_PLACE_BIRTH = ['', ' ', 'qwe#123', '~$!&?']

    # По полям паспорта  КИРГИЗИЯ
    LIST_POSITIVE_SERIES_PASSPORT_KYRGYZSTAN = ['DD', 'ZZ', 'AA']
    LIST_NEGATIVE_SERIES_PASSPORT_KYRGYZSTAN = ['dd', '', ' ', '1', '0', '123', '12345', 'qwer', 'йцук',
                                        'q', 'asdfg', 'фывап', 'ЙЦУКЕ', 'QWERT', '.123', '!2#$', '@-+()/":;']

    LIST_POSITIVE_NUNBER_DOC_PASSPORT_KYRGYZSTAN = ['1234567', '012345', '0000000']
    LIST_NEGATIVE_NUNBER_DOC_PASSPORT_KYRGYZSTAN = ['', ' ', '12345678', '01234567', 'qwe', 'йцуке', '1йцу', '1qwert', ]

    # По полям паспорта  ТАДЖИКИСТАН
    LIST_POSITIVE_NUNBER_DOC_PASSPORT_TAJIKISTAN = ['1234567', '012345', '123456789']
    LIST_NEGATIVE_NUNBER_DOC_PASSPORT_TAJIKISTAN = ['', ' ', '1234567890', '0123456789', 'qwe', 'йцуке', '1йцу', '1qwert', ]

    # По полям паспорта  ТАДЖИКИСТАН
    LIST_POSITIVE_NUNBER_DOC_PASSPORT_UZBEKISTAN = ['1234567', '012345', '0123456']
    LIST_NEGATIVE_NUNBER_DOC_PASSPORT_UZBEKISTAN = ['', ' ', '12345678', '01234567', 'qwe', 'йцуке', '1йцу', '1qwert', ]


    def documents_type(self, selector, field_text):
        if self.TYPE_MAIN_DOC_KYRGYZSTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_MAIN_DOC_KYRGYZSTAN.get(field_text))
        elif self.TYPE_MAIN_DOC_RUSSIA.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_MAIN_DOC_RUSSIA.get(field_text))
        elif self.TYPE_MAIN_DOC_TAJIKISTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_MAIN_DOC_TAJIKISTAN.get(field_text))
        elif self.TYPE_MAIN_DOC_UZBEKISTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_MAIN_DOC_UZBEKISTAN.get(field_text))
        else:
            value_list = []
        return value_list

    def documents_second_type(self, selector, field_text):
        if self.TYPE_SECOND_DOC_KYRGYZSTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_SECOND_DOC_KYRGYZSTAN.get(field_text))
        elif self.TYPE_SECOND_DOC_TAJIKISTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_SECOND_DOC_TAJIKISTAN.get(field_text))
        elif self.TYPE_SECOND_DOC_UZBEKISTAN.get(field_text):
            value_list = self.change_field_with_select(selector, self.TYPE_SECOND_DOC_UZBEKISTAN.get(field_text))
        else:
            value_list = []
        return value_list

    def select_of_client_by_citizenship(self, citizenship, filed_name):
        """Для подкидывая тестовых данных относитьльно гражданства и названия поля.
        На вход подается гражданство и название поля 'Номер', 'Серия' и т.д.
        На выходе политивный список и негативный список, и ФИО клиента который открывается"""
        positiv_list_validations = ''
        negativ_list_validations = ''
        if citizenship == 'РОССИЯ':
            text_for_search_old_client = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
            text_for_search_old_client_res = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES
            if filed_name == 'Серия':
                positiv_list_validations = self.LIST_POSITIVE_SERIES_PASSPORT_RF
                negativ_list_validations = self.LIST_NEGATIVE_SERIES_PASSPORT_RF
            if filed_name == 'Номер':
                positiv_list_validations = self.LIST_POSITIVE_NUNBER_DOC_PASSPORT_RF
                negativ_list_validations = self.LIST_NEGATIVE_NUNBER_DOC_PASSPORT_RF
        elif citizenship == 'ТАДЖИКИСТАН':
            text_for_search_old_client = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_TAJIKISTAN
            text_for_search_old_client_res = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_TAJIKISTAN_RES
            if filed_name == 'Серия':
                pass
            if filed_name == 'Номер':
                positiv_list_validations = self.LIST_POSITIVE_NUNBER_DOC_PASSPORT_TAJIKISTAN
                negativ_list_validations = self.LIST_NEGATIVE_NUNBER_DOC_PASSPORT_TAJIKISTAN
        elif citizenship == 'УЗБЕКИСТАН':
            text_for_search_old_client = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_UZBEKISTAN
            text_for_search_old_client_res = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_UZBEKISTAN_RES
            if filed_name == 'Серия':
                pass
            if filed_name == 'Номер':
                positiv_list_validations = self.LIST_POSITIVE_NUNBER_DOC_PASSPORT_UZBEKISTAN
                negativ_list_validations = self.LIST_NEGATIVE_NUNBER_DOC_PASSPORT_UZBEKISTAN
        else:# КИРГИЗИЯ
            text_for_search_old_client = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_KYRGYZSTAN
            text_for_search_old_client_res = self.TEXT_FOR_SEARCH_CLIENT_PASSPORT_KYRGYZSTAN_RES
            if filed_name == 'Серия':
                positiv_list_validations = self.LIST_POSITIVE_SERIES_PASSPORT_KYRGYZSTAN
                # negativ_list_validations = self.
            if filed_name == 'Номер':
                positiv_list_validations = self.LIST_POSITIVE_NUNBER_DOC_PASSPORT_KYRGYZSTAN
                negativ_list_validations = self.LIST_NEGATIVE_NUNBER_DOC_PASSPORT_KYRGYZSTAN
        return positiv_list_validations, negativ_list_validations, \
               text_for_search_old_client, text_for_search_old_client_res