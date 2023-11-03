import time
import pytest
import allure

from page_objects.PageLoginMP import PageLoginMP
from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation
from page_objects.ClientSearch import ClientSearch
from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation
from page_objects.ClientCardDocuments import ClientCardDocuments
from page_objects.ClientCardWorkAndIncomeExpenses import ClientCardWorkAndIncomeExpenses
from page_objects.ClientCardContactPersons import ClientCardContactPersons
from page_objects.ClientCardINNSNILS import ClientCardINNSNILS
from page_objects.ClientCardClientAddress import ClientCardClientAddress

@pytest.mark.page_search_client
@pytest.mark.regression
@allure.epic('Страница "Поиск клиента"')
@allure.title('Проверка наличия клиента')
def test_surname_text(mp, enable_notifications):
    """Проверяем наличие клиента в базе
    первая проверка, по номеру телефона,
    вторая, вводим данные и проверяем по ФИО
    Если успешно создается новый клиент"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
    page_mp = ClientSearch(mp)

    page_mp.click_element(page_mp.MENU_ADD)

    page_mp.clear_and_send_keys(page_mp.PHONE_NUMBER_TEXTVIEV_PARENT, page_mp.PHONE_NUMBER_TEXT, phone=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_SURNAME, page_mp.SURNAME_TEXT)
    page_mp.clear_and_send_keys(page_mp.CLIENT_NAME, page_mp.NAME_TEXT)
    page_mp.clear_and_send_keys(page_mp.PATRONYMIC_TEXTVIEV_PARENT, page_mp.PATRONYMIC_TEXTVIEV_PARENT_TEXT)
    page_mp.clear_and_send_keys(page_mp.DATE_OF_BIRTH_TEXTVIEV_PARENT, page_mp.DATE_OF_BIRTH_TEXT, date=True)

    button = page_mp.search_element(page_mp.FIND_CLIENT_BUTTON_PARENT)
    button.click()
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_SURNAME, page_mp.SURNAME_TEXT)

@pytest.mark.single_run_2
@pytest.mark.main_functionality
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.parametrize("citizenship_list", [['РОССИЯ', 'Тестфамилия', 'Росиия', '01012000',],
                                              ['КИРГИЗИЯ', 'Тестфамилия', 'Киргизия', '01012000',],
                                              ['ТАДЖИКИСТАН', 'Тестфамилия', 'Таджикистан', '01012000'],
                                              ['УЗБЕКИСТАН', 'Тестфамилия', 'Узбекистан', '01012000', ]])
@allure.epic("Основной Функционал")
@allure.title('Создание и сохранение нового клиента')
def test_save_new_client(mp, citizenship_list, enable_notifications):
    """Создать нового клиента на К15 с данными из метода customer_search_all_fields
    Заполнить все обязательные поля и сохранить"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
    page_mp = ClientSearch(mp)

    page_mp.click_element(page_mp.MENU_ADD)

    citizenship = citizenship_list[0]
    surname_text = citizenship_list[1]
    name_text = citizenship_list[2]
    # patronymic_textviev_parent_text = citizenship_list[3]
    patronymic_textviev_parent_text = page_mp.random_all(patronymic=True, len_srt=4)
    date_of_birth_text = citizenship_list[3]
    # phone_number_text = citizenship_list[5]
    phone_number_text = page_mp.random_all(phone=True)
    fio_text = surname_text + ' ' +  name_text + ' ' + patronymic_textviev_parent_text
    fio_text_down = fio_text.lower()

    # Заполение полей тестовыми данными на странице "Найти клиента"
    page_mp.clear_and_send_keys(page_mp.PHONE_NUMBER_TEXTVIEV_PARENT, phone_number_text, phone=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_SURNAME, surname_text)
    page_mp.clear_and_send_keys(page_mp.CLIENT_NAME, name_text)
    page_mp.clear_and_send_keys(page_mp.PATRONYMIC_TEXTVIEV_PARENT, patronymic_textviev_parent_text)
    page_mp.clear_and_send_keys(page_mp.DATE_OF_BIRTH_TEXTVIEV_PARENT, date_of_birth_text, date=True)
    page_mp.click_element(page_mp.FIND_CLIENT_BUTTON_PARENT)

    # Вкладка Общая информация
    page_mp = ClientCardGeneralInformation(mp)
    citizenship_selector = page_mp.CITIZENSHIP_DICT[citizenship]
    page_mp.text_field_new_client(page_mp.CLIENT_CARD_CITIZENSHIP)
    page_mp.click_element(page_mp.CLIENT_CARD_CITIZENSHIP)
    page_mp.click_element(citizenship_selector)
    page_mp.click_element(page_mp.CLIENT_CARD_GENDER_MALE)
    page_mp.click_element(page_mp.CLIENT_CARD_FAMILY_STATUS_OFFICIAL_MARRIAGE)
    page_mp.click_element(page_mp.CLIENT_CARD_EDUCATION_SECONDARY_TECHNICAL)
    page_mp.click_element(page_mp.CLIENT_CARD_LEARNED_THROUGH_FRIENDS)
    mp.hide_keyboard()

    time.sleep(1)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_EMAIL, page_mp.EMAIL_TEXT)
    mp.hide_keyboard()

    page_mp.click_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)

    page_mp = ClientCardClientAddress(mp)
    element_reg_adr = page_mp.search_element(page_mp.ENTER_ADDRESS)
    reg_address_text = page_mp.REGISTRATION_ADDRESS_TEXT_FIELD
    elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_reg_adr, reg_address_text)
    adress = elements_adress[0]
    adress.click()
    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS)

    page_mp.click_element(page_mp.SWITCH)
    mp.hide_keyboard()

    page_mp = ClientCardGeneralInformation(mp)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS, reg_address_text)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    mp.hide_keyboard()
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_OLD_LOAN, page_mp.OLD_LOAN_TEXT)
    mp.hide_keyboard()

    page_mp.click_element(page_mp.BUTTON_NEXT)

    # Вкладка Документы
    page_mp = ClientCardDocuments(mp)

    if citizenship == 'РОССИЯ':
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT_RF)
    else:
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT)

    if citizenship == 'РОССИЯ':
        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.DOC_SERIES_TEXT_RF)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.NUNBER_DOC, page_mp.DOC_NUNBER_DOC_TEXT)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.DOC_ISSUED_BY, page_mp.DOC_ISSUED_BY_TEXT_RF)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.DOC_DEPARTAMENT_CODE, page_mp.DEPARTAMENT_CODE_RF, phone=True)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_DOC1_DATE, page_mp.DOC1_DATE_TEXT, date=True)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    else:
        if citizenship != 'ТАДЖИКИСТАН':
            page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.DOC_SERIES_TEXT)
            mp.hide_keyboard()
            page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.NUNBER_DOC, page_mp.DOC_NUNBER_DOC_TEXT)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.DOC_ISSUED_BY, page_mp.DOC_ISSUED_BY_TEXT)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_DOC1_DATE, page_mp.DOC1_DATE_TEXT, date=True)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_DOC1_END_DATE, page_mp.DOC1_END_DATE_TEXT, date=True)
        mp.hide_keyboard()
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_PLACE_BIRTH, page_mp.PLACE_BIRTH_TEXT)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_PLACE_BIRTH, page_mp.PLACE_BIRTH_TEXT)
    mp.hide_keyboard()

    page_mp.click_element(page_mp.CLIENT_CARD_DOC_ADDRESS_HOMELAND)
    page_mp = ClientCardClientAddress(mp)
    page_mp.click_element(page_mp.ADDRESS_HOMELAND_COUNTRY)
    page_mp.click_element(page_mp.COUNTRY_TADJIKISTAN)

    # element_cc_full_address = page_mp.search_element(page_mp.COUNTRY_FULL_ADDRESS)
    # element_cc_full_address.clear()
    # page_mp = ClientCardDocuments(mp)
    page_mp.clear_and_send_keys(page_mp.COUNTRY_FULL_ADDRESS, page_mp.FULL_ADDRESS_TEXT)
    # element_cc_full_address.send_keys(page_mp.FULL_ADDRESS_TEXT)
    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS_2)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.click_element(page_mp.SWITCH)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp = ClientCardDocuments(mp)
    if citizenship == 'РОССИЯ':
        pass
    else:
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC)
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC_MIGR)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.SECOND_DOC_SERIES_TEXT)
        page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.SECOND_DOC_SERIES_TEXT)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.NUNBER_DOC, page_mp.SECOND_DOC_NUMBER_TEXT)
        page_mp.compare_text_in_field(page_mp.NUNBER_DOC, page_mp.SECOND_DOC_NUMBER_TEXT)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.DOC_ISSUED_BY, page_mp.SECOND_DOC_ISSUED_BY_TEXT)
        page_mp.compare_text_in_field(page_mp.DOC_ISSUED_BY, page_mp.SECOND_DOC_ISSUED_BY_TEXT)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_SECOND_DOC_DATE, page_mp.SECOND_DOC_DATE_TEXT, date=True)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_SECOND_DOC_END_DATE, page_mp.SECOND_DOC_END_DATE_TEXT, date=True)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.click_element(page_mp.BUTTON_NEXT)

    # Вкладка Работа и Доходы/расходы
    page_mp = ClientCardWorkAndIncomeExpenses(mp)
    page_mp.click_element(page_mp.CLIENT_CARD_JOB_ADRESS_JOB)
    page_mp = ClientCardClientAddress(mp)
    element_work_adr = page_mp.search_element(page_mp.ENTER_ADDRESS)
    work_address_text = page_mp.ADDRESS_PLACE_WORK_TEXT
    elements_work_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_work_adr, work_address_text)
    adress_work = elements_work_adress[0]
    adress_work.click()
    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS)

    page_mp = ClientCardWorkAndIncomeExpenses(mp)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_JOB_ADRESS_JOB, work_address_text)
    page_mp.click_element(page_mp.CLIENT_CARD_JOB_CATEGORY_POZITION)
    page_mp.click_element(page_mp.CATEGORY_POZITION_STREET_SWEEPER)
    mp.hide_keyboard()

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_POZITION, page_mp.POZITION_TEXT)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_PLACE_MAIN_INCOME, page_mp.PLACE_MAIN_INCOME_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_SUM_MAIN_INCOME, page_mp.SUM_MAIN_INCOME_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_EXPERIENCE, page_mp.EXPERIENCE_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.CLIENT_CARD_JOB_SOURCE_ADDITIONALINCOME)
    page_mp.click_element(page_mp.SOURCE_ADDITIONALINCOME_PART_TIME_JOB)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_SUM_ADDITIONAL_INCOME, page_mp.SUM_ADDITIONAL_INCOME_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ADVANCE_PAYMENT_DATE, page_mp.ADVANCE_PAYMENT_DATE_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_PAYDAY, page_mp.PAYDAY_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS, page_mp.CURRENT_OBLIGATIONS_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS_SUM, page_mp.CURRENT_OBLIGATIONS_SUM_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS, page_mp.ALIMONY_OBLIGATIONS_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS_SUM, page_mp.ALIMONY_OBLIGATIONS_SUM_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES, page_mp.OTHER_EXPENSES_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES_SUM, page_mp.OTHER_EXPENSES_SUM_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.BUTTON_NEXT)

    # Вкладка Контактные лица
    page_mp = ClientCardContactPersons(mp)
    page_mp.click_element(page_mp.CONTACT_PERSONS_BUTTON_NEW_CONTACT)

    page_mp.click_element(page_mp.CONTACT_PERSONS_NEW_TYPE_CONNECTION)
    page_mp.click_element(page_mp.NEW_TYPE_CONNECTION_BROTHER)
    mp.hide_keyboard()

    page_mp.clear_and_send_keys(page_mp.CONTACT_PERSONS_NEW_FIO, page_mp.CONTACT_NEW_FIO_TEXT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CONTACT_PERSONS_PHONE_NUMBER, page_mp.CONTACT_PHONE_NUMBER_TEXT, phone=True)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.BUTTON_SAVE)

    page_mp.click_element(page_mp.BUTTON_NEXT)

    # Вкладка ИНН/СНИЛС
    page_mp = ClientCardINNSNILS(mp)
    if citizenship == 'РОССИЯ':
        page_mp.clear_and_send_keys(page_mp.INN_TEXT_FIELD, page_mp.INN_CLIENT)
        page_mp.clear_and_send_keys(page_mp.SNILS_TEXT_FIELD, page_mp.SNILS_CLIENT)
    else:
        elements_inn_snils = page_mp.search_all_elements(page_mp.INN_SNILS_CROSS)
        elements_inn_snils[0].click()
        elements_inn_snils[1].click()

    # Сохранение крточки клиента
    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD, wait_time=20)
    time.sleep(1)

    page_mp.click_element(page_mp.MENU_MY_CLIENTS, wait_time=20)
    page_mp.click_element(page_mp.MY_CLIENTS_MENU_ALL)
    page_mp.clear_and_send_keys(page_mp.EDIT_TEXT_SEARH_CLIENT, fio_text_down, compare_text_in_field=False)
    element_fio_client = page_mp.search_all_elements(page_mp.FIO_CLIENT_ALL_CLIENTS)
    assert element_fio_client[0].text == fio_text

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.parametrize("citizenship_list", [['РОССИЯ', 'Тестфамилия', 'Россия', 'Тестотчество', '01012000', '79310000013'],
                                              ['КИРГИЗИЯ', 'Тестфамилия', 'Киргизия', 'Тестотчество', '01012000', '79310000010'],
                                              ['ТАДЖИКИСТАН', 'Тестфамилия', 'Таджикистан', 'Тестотчество', '01012000', '79310000011'],
                                              ['УЗБЕКИСТАН', 'Тестфамилия', 'Узбекистан', 'Тестотчество', '01012000', '79310000012']
                                              ])
@allure.epic("Основной Функционал")
@allure.title('Заполнение основного документа по фото у нового клиента')
def test_new_client_photo_doc(mp, citizenship_list, enable_notifications):
    """Проверка заполнения полей документа по фото у нового клиента"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientSearch(mp)
    page_mp.click_element(page_mp.MENU_ADD)

    citizenship = citizenship_list[0]
    surname_text = citizenship_list[1]
    name_text = citizenship_list[2]
    # patronymic_textviev_parent_text = citizenship_list[3]
    patronymic_textviev_parent_text = page_mp.random_all(patronymic=True, len_srt=4)
    date_of_birth_text = citizenship_list[4]
    # phone_number_text = citizenship_list[5]
    phone_number_text = page_mp.random_all(phone=True)
    fio_text = surname_text + ' ' +  name_text + ' ' + patronymic_textviev_parent_text
    fio_text_down = fio_text.lower()

    # Заполение полей тестовыми данными на странице "Найти клиента"
    page_mp.clear_and_send_keys(page_mp.PHONE_NUMBER_TEXTVIEV_PARENT, phone_number_text, phone=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_SURNAME, surname_text)
    page_mp.clear_and_send_keys(page_mp.CLIENT_NAME, name_text)
    page_mp.clear_and_send_keys(page_mp.PATRONYMIC_TEXTVIEV_PARENT, patronymic_textviev_parent_text)
    page_mp.clear_and_send_keys(page_mp.DATE_OF_BIRTH_TEXTVIEV_PARENT, date_of_birth_text, date=True)
    page_mp.click_element(page_mp.FIND_CLIENT_BUTTON_PARENT)

    # Вкладка Общая информация
    page_mp = ClientCardGeneralInformation(mp)
    citizenship_selector = page_mp.CITIZENSHIP_DICT[citizenship]
    page_mp.text_field_new_client(page_mp.CLIENT_CARD_CITIZENSHIP)
    page_mp.click_element(page_mp.CLIENT_CARD_CITIZENSHIP)
    page_mp.click_element(citizenship_selector)
    page_mp.click_element(page_mp.CANCEL_BUTTUN)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    # Вкладка Документы
    page_mp = ClientCardDocuments(mp)

    series_doc = ' '
    number_doc = ' '
    issued_by_doc = '  '
    deportament_code = ' '
    date_doc = ' '
    date_end_doc = ' '

    if citizenship == 'РОССИЯ':
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT_RF)
    else:
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
        page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT)

    if citizenship == 'РОССИЯ':
        series_doc = '4511'
        number_doc = '821700'
        issued_by_doc = 'покровское-стрешнево'
        deportament_code = '770-094'
        date_doc = '13.09.2011'
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
        selector_name_photo = page_mp.get_selector_by_text(page_mp.DOCUMENT_TYPS_RUSSIA[1])
        page_mp.click_element(selector_name_photo)

    if citizenship == 'КИРГИЗИЯ':
        series_doc = 'AC'
        number_doc = '2903633'
        issued_by_doc = ''
        date_doc = '15.03.2017'
        date_end_doc = '15.03.2027'
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
        selector_name_photo = page_mp.get_selector_by_text(page_mp.DOCUMENT_TYPS_KYRGYZSTAN[1])
        page_mp.click_element(selector_name_photo)

    if citizenship == 'ТАДЖИКИСТАН':
        series_doc = ''
        number_doc = '403095222'
        issued_by_doc = ''
        date_doc = '17.06.2010'
        date_end_doc = '16.06.2030'
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
        selector_name_photo = page_mp.get_selector_by_text(page_mp.DOCUMENT_TYPS_TAJIKISTAN[1])
        page_mp.click_element(selector_name_photo)

    if citizenship == 'УЗБЕКИСТАН':
        series_doc = 'FA'
        number_doc = '1754314'
        issued_by_doc = ''
        date_doc = '11.01.2011'
        date_end_doc = '10.01.2031'
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
        selector_name_photo = page_mp.get_selector_by_text(page_mp.DOCUMENT_TYPS_TAJIKISTAN[1])
        page_mp.click_element(selector_name_photo)

    if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
        page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)
    page_mp.click_element(page_mp.SELECT_PHOTO_FROM_DEVICES)

    if citizenship == 'РОССИЯ':
        el = page_mp.search_all_elements(page_mp.PHOHO_ALL_GALLERY)
        page_mp.click_element(el[page_mp.PHOTO_PASSPORT_RUSSIA])
        page_mp.logger.info(f"el len = {len(el)}")
    if citizenship == 'КИРГИЗИЯ':
        el = page_mp.search_all_elements(page_mp.PHOHO_ALL_GALLERY)
        page_mp.click_element(el[page_mp.PHOTO_PASSPORT_KYRGYZSTAN])
    if citizenship == 'ТАДЖИКИСТАН':
        el = page_mp.search_all_elements(page_mp.PHOHO_ALL_GALLERY)
        page_mp.click_element(el[page_mp.PHOTO_PASSPORT_TAJIKISTAN])
    if citizenship == 'УЗБЕКИСТАН':
        el = page_mp.search_all_elements(page_mp.PHOHO_ALL_GALLERY)
        page_mp.click_element(el[page_mp.PHOTO_PASSPORT_UZBEKISTAN])

    if not citizenship == 'ТАДЖИКИСТАН':
        page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_SERIES, series_doc, wait_time=12)
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.compare_text_in_field(page_mp.NUNBER_DOC, number_doc, wait_time=12)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    if citizenship == 'РОССИЯ':
        page_mp.compare_text_in_field(page_mp.DOC_DEPARTAMENT_CODE, deportament_code)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_DOC1_DATE, date_doc)
    if not citizenship == 'РОССИЯ':
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_DOC1_END_DATE, date_end_doc)
    time.sleep(3)
