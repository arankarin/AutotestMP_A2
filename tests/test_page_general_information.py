import time
import pytest
import allure

from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation
from page_objects.PageLoginMP import PageLoginMP

@pytest.mark.page_general_information
@pytest.mark.regression
@allure.epic('КК Страница "Общая информация"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Гражданство"')
def test_field_with_selection_citizenship(mp, enable_notifications):
    """Проверка поля, 'Гражданство'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.click_element(page_mp.CLIENT_CARD_CITIZENSHIP)
    page_mp.select_field_value(page_mp.CLIENT_CARD_CITIZENSHIP, page_mp.CITIZENSHIP)

@pytest.mark.page_general_information
@pytest.mark.regression
@allure.epic('КК Страница "Общая информация"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Пол"')
def test_field_with_selection_gender(mp, enable_notifications):
    """Проверка поля, 'Пол'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.click_element(page_mp.CLIENT_CARD_GENDER)
    page_mp.select_field_value(page_mp.CLIENT_CARD_GENDER, page_mp.GENDER)

@pytest.mark.page_general_information
@pytest.mark.regression
@allure.epic('КК Страница "Общая информация"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Семейное положение"')
def test_field_with_selection_family(mp, enable_notifications):
    """Проверка поля, 'Семейное положение'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.click_element(page_mp.CLIENT_CARD_FAMILY)
    page_mp.select_field_value(page_mp.CLIENT_CARD_FAMILY, page_mp.FAMILY)

@pytest.mark.page_general_information
@pytest.mark.regression
@allure.epic('КК Страница "Общая информация"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "Образование"')
def test_field_with_selection_education(mp, enable_notifications):
    """Проверка поля, 'Образование'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME, selector_scroll_to_element=page_mp.CLIENT_CARD_EDUCATION)

    page_mp.click_element(page_mp.CLIENT_CARD_EDUCATION)
    page_mp.select_field_value(page_mp.CLIENT_CARD_EDUCATION, page_mp.EDUCATION)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)


@pytest.mark.page_general_information
@pytest.mark.regression
@allure.epic('КК Страница "Общая информация"')
@allure.feature('Поля с выбором')
@allure.title('Проверка поля, "О нас узнали через"')
def test_field_with_selection_throught(mp, enable_notifications):
    """Проверка поля, 'О нас узнали через'.
    Проверка поля с выбором на существующем клиенте клиенте,
    проверка производится всех вариантов из списка выбора"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME, selector_scroll_to_element=page_mp.CLIENT_CARD_FOUND_THROUGHT)
    page_mp.click_element(page_mp.CLIENT_CARD_FOUND_THROUGHT)
    page_mp.select_field_value(page_mp.CLIENT_CARD_FOUND_THROUGHT, page_mp.FOUND_THROUGHT)

@pytest.mark.with_parameters
@pytest.mark.validation
@pytest.mark.positive
@allure.epic('КК Страница "Общая информация"')
@allure.feature('С параметрами')
@allure.story('"Адрес электронной почты"')
@pytest.mark.page_general_information
@allure.title('"Адрес электронной почты" Позитивный тест')
def test_positive_email(mp, params_positive_mail, enable_notifications):
    """Позитивня проверка поля 'Адрес электронной почты'"""
    text = params_positive_mail
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN,
                        scroll_page_selector=page_mp.HEADING_GENERAL_INFORMATION,
                        selector_scroll_to_element=page_mp.CLIENT_CARD_EMAIL)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_EMAIL, text)
    page_mp.positive_assert_validation_field_location(page_mp.CLIENT_CARD_EMAIL_VALIDATION, page_mp.CLIENT_CARD_EMAIL,
                                                      text=text, wait_time=0.1)


@pytest.mark.with_parameters
@pytest.mark.validation
@pytest.mark.negative
@allure.epic('КК Страница "Общая информация"')
@allure.feature('С параметрами')
@allure.story('"Адрес электронной почты"')
@pytest.mark.page_general_information
@allure.title('"Адрес электронной почты" Негативный тест')
def test_negative_email(mp, params_negative_mail, enable_notifications):
    """Негативная проверка поля 'Адрес электронной почты'"""
    text = params_negative_mail
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN,
                        scroll_page_selector=page_mp.HEADING_GENERAL_INFORMATION,
                        selector_scroll_to_element=page_mp.CLIENT_CARD_EMAIL)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_EMAIL, text)
    mp.hide_keyboard()
    page_mp.negetive_assert_validation_field_location(page_mp.CLIENT_CARD_EMAIL_VALIDATION, page_mp.CLIENT_CARD_EMAIL,
                                                      text=text, wait_time=0.1)

@pytest.mark.with_parameters
@pytest.mark.validation
@pytest.mark.positive
@pytest.mark.page_general_information
@allure.epic('КК Страница "Общая информация"')
@allure.feature('С параметрами')
@allure.story('"Предыдущие займ"')
@allure.title('"Предыдущие займы" Позитивный тест')
def test_positive_old_loan(mp, params_positive_old_loan, enable_notifications):
    """Позитивня проверка поля 'Предыдущие займы'"""
    text = params_positive_old_loan
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN,
                        scroll_page_selector=page_mp.HEADING_GENERAL_INFORMATION,
                        selector_scroll_to_element=page_mp.CLIENT_CARD_OLD_LOAN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_OLD_LOAN, text)
    page_mp.positive_assert_validation_field_location(page_mp.CLIENT_CARD_OLD_LOAN_VALIDATION, page_mp.CLIENT_CARD_OLD_LOAN,
                                                      text=text, wait_time=0.1)

@pytest.mark.page_general_information
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Общая информация"')
@allure.title('Проверка отображения ФИО и номера телефона, на странице "Общая информация"')
def test_fio_birthday_and_number(mp, enable_notifications):
    """Проверка верного отображения ФИО и номера телефона"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)

    surname, name, patronymic = page_mp.split_fio(page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_SURNAME, surname)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_NAME, name)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_PATRONYMIC, patronymic)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_MAIN_PHONE, page_mp.PHONE_NUMBER_OLD_CLIENT_TEXT, phone=True)
