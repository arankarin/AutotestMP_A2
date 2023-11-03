import time
import pytest
import allure

from page_objects.ClientCardDocuments import ClientCardDocuments
from page_objects.PageLoginMP import PageLoginMP
from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation

@pytest.mark.page_documents
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Тип основного документа"')
def test_field_with_selection_type_main_doc_(mp, enable_notifications):
    """Проверка поля, 'Тип основного документа'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp = ClientCardDocuments(mp)

    page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
    page_mp.select_field_value(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC,
                               page_mp.TYPE_MAIN_DOC_TAJIKISTAN['ТАДЖИКИСТАН'])


@pytest.mark.page_documents
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Тип дополнительного документа"')
def test_field_with_selection_type_second_doc(mp, enable_notifications):
    """Проверка поля, 'Тип дополнительного документа'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp = ClientCardDocuments(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN,
                        scroll_page_selector=page_mp.HEADING_DOCUMENTS,
                        selector_scroll_to_element=page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC)
    page_mp.select_field_value(page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC,
                               page_mp.TYPE_SECOND_DOC_TAJIKISTAN['ТАДЖИКИСТАН'])


@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Серия основного документа" Паспорт РФ')
def test_validation_series_fields_passport_rf(mp, enable_notifications):
    """Проверка валидации "Серия основного документа" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)
    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    # Проверка серии документа
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.CLIENT_CARD_DOC_SERIES_VALIDATION,
                              page_mp.LIST_POSITIVE_SERIES_PASSPORT_RF, validation='positive')
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_SERIES, page_mp.CLIENT_CARD_DOC_SERIES_VALIDATION,
                              page_mp.LIST_NEGATIVE_SERIES_PASSPORT_RF, validation='negetive')



@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@pytest.mark.parametrize("citizenship", ['РОССИЯ', 'КИРГИЗИЯ', 'УЗБЕКИСТАН', 'ТАДЖИКИСТАН'])
@pytest.mark.parametrize("filed_name", ['Номер'])
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Номер основного документа" Паспорт РФ')
def test_validation_number_fields_passport_rf(mp, enable_notifications, citizenship, filed_name):
    """Проверка валидации "Номер основного документа" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)

    field_name = page_mp.NUNBER_DOC
    field_validation = page_mp.NUNBER_DOC_VALIDATION

    positiv_list_validations, negativ_list_validations, \
    text_for_search_old_client, text_for_search_old_client_res = page_mp.select_of_client_by_citizenship(citizenship, filed_name)

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, page_mp.MENU_DOCUMENTS, field_name)

    # Проверка номера документа
    page_mp.validations_field(field_name, field_validation, positiv_list_validations, validation='positive')
    page_mp.validations_field(field_name, field_validation, negativ_list_validations, validation='negetive')



@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Кем выдан основной документ" Паспорт РФ')
def test_validation_issued_by_fields_passport_rf(mp, enable_notifications):
    """Проверка валидации "Кем выдан основной документ" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)
    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    # Проверка кем выдан документ
    page_mp.validations_field(page_mp.DOC_ISSUED_BY, page_mp.DOC_ISSUED_BY_VALIDATION,
                              page_mp.LIST_POSITIVE_DOC_ISSUED_BY_PASSPORT_RF, validation='positive')
    page_mp.validations_field(page_mp.DOC_ISSUED_BY, page_mp.DOC_ISSUED_BY_VALIDATION,
                              page_mp.LIST_NEGATIVE_DOC_ISSUED_BY_PASSPORT_RF, validation='negetive')


@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Код подразделения основной документ" Паспорт РФ')
def test_validation_departament_code_fields_passport_rf(mp, enable_notifications):
    """Проверка валидации "Код подразделения основной документ" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)
    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, page_mp.MENU_DOCUMENTS, page_mp.DOC_DEPARTAMENT_CODE)

    # Проверка код подразделения
    page_mp.validations_field(page_mp.DOC_DEPARTAMENT_CODE, page_mp.DOC_DEPARTAMENT_CODE_VALIDATION,
                              page_mp.LIST_POSITIVE_DEPARTAMENT_CODE, validation='positive', phone=True)
    page_mp.validations_field(page_mp.DOC_DEPARTAMENT_CODE, page_mp.DOC_DEPARTAMENT_CODE_VALIDATION,
                              page_mp.LIST_NEGATIVE_DEPARTAMENT_CODE, validation='negetive')

# КОГДА ЛОКАТОР ПОЛЯ В
@pytest.mark.skip(reason="Пока не починим локатор на поле валидации у даты основного документа")
@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Дата выдачи  основной документ" Паспорт РФ')
def test_validation_doc_date_fields_passport_rf(mp, enable_notifications):
    """Проверка валидации "Дата выдачи основной документ" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)
    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, page_mp.MENU_DOCUMENTS, page_mp.CLIENT_CARD_DOC_DOC1_DATE)

    # Проверка код подразделения
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_DOC1_DATE, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH_VALIDATION,
                              page_mp.LIST_POSITIVE_DEPARTAMENT_CODE, validation='positive')
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_DOC1_DATE, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH_VALIDATION,
                              page_mp.LIST_NEGATIVE_DEPARTAMENT_CODE, validation='negetive')



@pytest.mark.page_documents
@pytest.mark.validation
@pytest.mark.regression
@allure.epic('КК Страница "Документы"')
@allure.feature('Поля основного докумеента')
@allure.title('Проверка валидации "Место рождения" Паспорт РФ')
def test_validation_place_birth_fields_passport_rf(mp, enable_notifications):
    """Проверка валидации "Место рождения" Паспорт РФ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardDocuments(mp)
    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PASSPORT_RF_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res, search_accurate=False)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, page_mp.MENU_DOCUMENTS, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH)

    # Проверка код подразделения
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_PLACE_BIRTH, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH_VALIDATION,
                              page_mp.LIST_POSITIVE_PLACE_BIRTH, validation='positive')
    page_mp.validations_field(page_mp.CLIENT_CARD_DOC_PLACE_BIRTH, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH_VALIDATION,
                              page_mp.LIST_NEGATIVE_PLACE_BIRTH, validation='negetive')
