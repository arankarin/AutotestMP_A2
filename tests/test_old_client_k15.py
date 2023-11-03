import time
import pytest
import allure

from page_objects.MainPages import MainPage
from page_objects.PageLoginMP import PageLoginMP
from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation
from page_objects.ClientCardDocuments import ClientCardDocuments
from page_objects.ClientCardOtherDocuments import ClientCardOtherDocuments
from page_objects.ClientCardWorkAndIncomeExpenses import ClientCardWorkAndIncomeExpenses
from page_objects.ClientCardContactPersons import ClientCardContactPersons
from page_objects.ClientCardINNSNILS import ClientCardINNSNILS
from page_objects.ClientCardApplicationsAndContracts import ClientCardApplicationsAndContracts
from page_objects.ClientCardClientAddress import ClientCardClientAddress
from page_objects.ClientCardASP import ClientCardASP
from page_objects.ClientCardVisitInspeckion import ClientCardVisitInspeckion

@pytest.mark.main_functionality
@pytest.mark.regression
@pytest.mark.sanity
# @pytest.mark.skip(reason="На К15 сломаны заявки")
@allure.feature("Основной Функционал")
@allure.title('Создание заявки')
def test_new_create_request_for_loan(mp, enable_notifications):
    """Создать новую заявку на К15 на займ клиенту Тестфамилия Заявка Тестотчество
    Заполнить все обязательные поля и сохранить"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_DEMO, page_mp.PASSWORD_VOROBEV)
    page_mp = ClientCardApplicationsAndContracts(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN_DEMO
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_REQUEST_LOAN_RES_DEMO

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_APPLICATIONS_AND_CONTRACTS)
    page_mp.click_element(page_mp.MENU_APPLICATIONS_AND_CONTRACTS)
    page_mp.click_element(page_mp.BUTTON_NEW_CONTRACT)
    page_mp.click_element(page_mp.APPLICATIONS_AND_CONTRACTS_DIRECTION_LOAN_EXPENDITURE)
    page_mp.click_element(page_mp.DIRECTION_LOAN_EXPENDITURE_PERSONAL_TARGET)
    page_mp.click_element(page_mp.VIEW_CONTRACTS_IVDIVIDUAL1)

    page_mp.clear_and_send_keys(page_mp.DESIRED_DAY_PAYMENT, page_mp.TEXT_DESIRED_DAY_PAYMENT)
    mp.hide_keyboard()
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.LOAN_TERM, page_mp.TEXT_LOAN_TERM)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.SUMM_CONTRACT, page_mp.TEXT_SUMM_CONTRACT)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    mp.hide_keyboard()

    page_mp.click_element(page_mp.BUTTON_CREATE_LOAN_APPLICATION)
    time.sleep(10) # Только на демо базе

    page_mp.click_element(page_mp.MENU_MY_APPLICATIONS)

    elements_fio_clients_my_application = page_mp.search_all_elements(page_mp.MY_APPLICATIONS_FIO_CLIENTS)
    page_mp.search_text_in_elements(elements_fio_clients_my_application, text_for_search_old_client_res)

@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Общая информация"')
@allure.title('Изменение существующей карточки, страница "Общая информация"')
def test_changing_on_old_client_general_information(mp, enable_notifications):
    """Изменение на вкладке "Общая информация"  существующего клиента и сохранение"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = MainPage(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    # Общая информация
    value_list_general = []
    page_mp = ClientCardGeneralInformation(mp)

    # #Гражданство не меняем, иначе данныее паспортов сотрутся на странице "Документы"
    # value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_CITIZENSHIP, page_mp.CITIZENSHIP)
    # value_list_general.append(value_list)

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_GENDER, page_mp.GENDER)
    value_list_general.append(value_list)

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_FAMILY, page_mp.FAMILY)
    value_list_general.append(value_list)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_EDUCATION, page_mp.EDUCATION)
    value_list_general.append(value_list)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_FOUND_THROUGHT, page_mp.FOUND_THROUGHT)
    value_list_general.append(value_list)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    email = page_mp.random_email()
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_EMAIL, email)
    value_list_general.append([email, page_mp.CLIENT_CARD_EMAIL])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    element = page_mp.search_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    element_text = element.text

    page_mp.click_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    page_mp = ClientCardClientAddress(mp)
    element_reg_adr = page_mp.search_element(page_mp.ENTER_ADDRESS)
    if element_text == page_mp.REGISTRATION_ADDRESS_TEXT_FIELD:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_reg_adr,
                                                   page_mp.REGISTRATION_ADDRESS_TEXT_NEW_FIELD)
    else:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_reg_adr,
                                                   page_mp.REGISTRATION_ADDRESS_TEXT_FIELD)
    adress = elements_adress[0]
    adress.click()

    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp = ClientCardGeneralInformation(mp)
    element_text_new = page_mp.search_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    value_list_general.append([element_text_new.text, page_mp.CLIENT_CARD_REGISTRATION_ADDRESS])

    if page_mp.field_presence_check(page_mp.CLIENT_CARD_FACT_ADDRESS):
        pass
    else:
        page_mp.click_element(page_mp.SWITCH)

    element = page_mp.search_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    element_text = element.text

    page_mp.click_element(page_mp.CLIENT_CARD_FACT_ADDRESS)
    page_mp = ClientCardClientAddress(mp)
    element_fact_adr = page_mp.search_element(page_mp.ENTER_ADDRESS)
    if element_text == page_mp.REGISTRATION_ADDRESS_TEXT_FIELD:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_fact_adr,
                                                   page_mp.REGISTRATION_ADDRESS_TEXT_NEW_FIELD)
    else:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_fact_adr,
                                                   page_mp.REGISTRATION_ADDRESS_TEXT_FIELD)
    adress = elements_adress[0]
    adress.click()
    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp = ClientCardGeneralInformation(mp)
    element_text_new = page_mp.search_element(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    value_list_general.append([element_text_new.text, page_mp.CLIENT_CARD_REGISTRATION_ADDRESS])

    text_old_loan = page_mp.random_all(str_latin=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_OLD_LOAN, text_old_loan)
    value_list_general.append([text_old_loan, page_mp.CLIENT_CARD_OLD_LOAN])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(3)

    # После созранения крточки, открываем ее и проверяем заполенение полей
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    for element_list in value_list_general:
        if page_mp.field_presence_check(element_list[1]):
            pass
        else:
            page_mp.scrolls_all(page_mp.SCROLL_DOWN)
            page_mp.scrolls_all(page_mp.SCROLL_DOWN)
            page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        text_field = page_mp.check_text_by_selector(element_list[1])
        assert text_field == element_list[0]


@pytest.mark.page_documents
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Документы"')
@allure.title('Изменение существующей карточки, страница "Документы"')
def test_changing_on_old_client_documents(mp, enable_notifications):
    """Изменение на вкладке "Документы"  существующего клиента и сохранение"""
    value_list_documents = []
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = MainPage(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)
    citizenship_field = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_CITIZENSHIP)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp = ClientCardDocuments(mp)
    value_list = page_mp.documents_type(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC, citizenship_field)
    value_list_documents.append(value_list)

    if citizenship_field == page_mp.KYRGYZSTAN or citizenship_field == page_mp.UZBEKISTAN or citizenship_field == page_mp.RUSSIA:
        text_series_doc = ''
        if citizenship_field == page_mp.KYRGYZSTAN or citizenship_field == page_mp.UZBEKISTAN:
            text_series_doc = page_mp.random_all(series=True, len_srt=2)
        elif citizenship_field == page_mp.RUSSIA:
            text_series_doc = page_mp.random_all(nuber=True, len_srt=4)
        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_SERIES, text_series_doc)
        value_list_documents.append([text_series_doc, page_mp.CLIENT_CARD_DOC_SERIES])
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_number_doc = page_mp.random_all(nuber=True, len_srt=4)
    page_mp.clear_and_send_keys(page_mp.NUNBER_DOC, text_number_doc)
    value_list_documents.append([text_number_doc, page_mp.NUNBER_DOC])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_issued_by = page_mp.random_all(str_latin=True, len_srt=5)
    page_mp.clear_and_send_keys(page_mp.DOC_ISSUED_BY, text_issued_by)
    value_list_documents.append([text_issued_by, page_mp.DOC_ISSUED_BY])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_DOC1_DATE, page_mp.DOC1_DATE_TEXT, date=True)
    value_list_documents.append([page_mp.DOC1_DATE_TEXT_IN_FIELD, page_mp.CLIENT_CARD_DOC_DOC1_DATE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_DOC1_END_DATE, page_mp.DOC1_END_DATE_TEXT, date=True)
    value_list_documents.append([page_mp.DOC1_END_DATE_TEXT_IN_FIELD, page_mp.CLIENT_CARD_DOC_DOC1_END_DATE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_place_birht = page_mp.random_all(str_latin=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_PLACE_BIRTH, text_place_birht)
    value_list_documents.append([text_place_birht, page_mp.CLIENT_CARD_DOC_PLACE_BIRTH])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.CLIENT_CARD_DOC_ADDRESS_HOMELAND)

    page_mp = ClientCardGeneralInformation(mp)
    citizenship_list = page_mp.CITIZENSHIP

    page_mp = ClientCardClientAddress(mp)
    page_mp.change_field_with_select(page_mp.ADDRESS_HOMELAND_COUNTRY, citizenship_list)

    text_place_full_addess = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.COUNTRY_FULL_ADDRESS, text_place_full_addess)

    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS_2)

    page_mp = ClientCardDocuments(mp)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_ADDRESS_HOMELAND, text_place_full_addess)
    value_list_documents.append([text_place_full_addess, page_mp.CLIENT_CARD_DOC_ADDRESS_HOMELAND])


    if page_mp.field_presence_check(page_mp.CLIENT_CARD_DOC_FACT_ADDRESS_HOMELAND):
        pass
    else:
        page_mp.click_element(page_mp.SWITCH)

    page_mp.click_element(page_mp.CLIENT_CARD_DOC_FACT_ADDRESS_HOMELAND)

    page_mp = ClientCardClientAddress(mp)
    value_list = page_mp.change_field_with_select(page_mp.ADDRESS_HOMELAND_COUNTRY, citizenship_list)

    text_place_full_addess = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.COUNTRY_FULL_ADDRESS, text_place_full_addess)

    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS_2)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp = ClientCardDocuments(mp)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_DOC_FACT_ADDRESS_HOMELAND, text_place_full_addess)
    value_list_documents.append([text_place_full_addess, page_mp.CLIENT_CARD_DOC_FACT_ADDRESS_HOMELAND])
    # page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    value_list = page_mp.documents_second_type(page_mp.CLIENT_CARD_DOC_TYPE_SECOND_DOC, citizenship_field)
    value_list_documents.append(value_list)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_second_eries_doc = page_mp.random_all(series=True, len_srt=2)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_DOC_SERIES, text_second_eries_doc)
    value_list_documents.append([text_second_eries_doc, page_mp.CLIENT_CARD_DOC_SERIES])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_number_doc = page_mp.random_all(nuber=True, len_srt=4)
    page_mp.clear_and_send_keys(page_mp.NUNBER_DOC, text_number_doc)
    value_list_documents.append([text_number_doc, page_mp.NUNBER_DOC])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_issued_by = page_mp.random_all(str_latin=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.DOC_ISSUED_BY, text_issued_by)
    value_list_documents.append([text_issued_by, page_mp.DOC_ISSUED_BY])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_SECOND_DOC_DATE, page_mp.SECOND_DOC_DATE_TEXT, date=True)
    value_list_documents.append([page_mp.SECOND_DOC_DATE_TEXT_IN_FIELD, page_mp.CLIENT_CARD_SECOND_DOC_DATE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_SECOND_DOC_END_DATE, page_mp.SECOND_DOC_END_DATE_TEXT, date=True)
    value_list_documents.append([page_mp.SECOND_DOC_END_DATE_TEXT_IN_FIELD, page_mp.CLIENT_CARD_SECOND_DOC_END_DATE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(3)

    # После созранения крточки, открываем ее и проверяем заполенение полей
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.click_element(page_mp.MENU_DOCUMENTS)

    page_mp.checking_field_values_from_list(value_list_documents)

@pytest.mark.page_work_and_income_expenses
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Работа и Доходы/расходы"')
@allure.title('Изменение существующей карточки, страница "Работа и Доходы/расходы"')
def test_changing_on_old_client_work_income(mp, enable_notifications):
    """Изменение на вкладке "Работа и Доходы/расходы"  существующего клиента и сохранение"""
    value_list_work_income = []
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = MainPage(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.click_element(page_mp.MENU_WORK_AND_INCOME)

    page_mp = ClientCardWorkAndIncomeExpenses(mp)
    element = page_mp.search_element(page_mp.CLIENT_CARD_JOB_ADRESS_JOB)
    element_text = element.text

    page_mp.click_element(page_mp.CLIENT_CARD_JOB_ADRESS_JOB)
    page_mp = ClientCardClientAddress(mp)
    element_reg_adr = page_mp.search_element(page_mp.ENTER_ADDRESS)
    if element_text == page_mp.ADDRESS_PLACE_WORK_TEXT:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_reg_adr,
                                                   page_mp.ADDRESS_PLACE_WORK_TEXT_NEW)
    else:
        elements_adress = page_mp.search_addresses(page_mp.ALL_REGISTRATION_ADDRESS, element_reg_adr,
                                                   page_mp.ADDRESS_PLACE_WORK_TEXT)
    adress = elements_adress[0]
    adress.click()

    page_mp.click_element(page_mp.BUTTON_SAVE_ADDRESS)

    page_mp = ClientCardWorkAndIncomeExpenses(mp)
    text_address_job = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_JOB_ADRESS_JOB)
    value_list_work_income.append([text_address_job, page_mp.CLIENT_CARD_JOB_ADRESS_JOB])

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_JOB_CATEGORY_POZITION, page_mp.CATEGORY_POZITION)
    value_list_work_income.append(value_list)

    text_pozition = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_POZITION, text_pozition)
    value_list_work_income.append([text_pozition, page_mp.CLIENT_CARD_JOB_POZITION])

    text_place_main_income = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_PLACE_MAIN_INCOME, text_place_main_income)
    value_list_work_income.append([text_place_main_income, page_mp.CLIENT_CARD_JOB_PLACE_MAIN_INCOME])

    text_sum_main_income = page_mp.random_all(nuber=True, len_srt=5)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_SUM_MAIN_INCOME, text_sum_main_income)
    value_list_work_income.append([text_sum_main_income, page_mp.CLIENT_CARD_JOB_SUM_MAIN_INCOME])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_sum_job_experience = page_mp.random_all(day=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_EXPERIENCE, text_sum_job_experience)
    value_list_work_income.append([text_sum_job_experience, page_mp.CLIENT_CARD_JOB_EXPERIENCE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    value_list = page_mp.change_field_with_select(page_mp.CLIENT_CARD_JOB_SOURCE_ADDITIONALINCOME, page_mp.SOURCE_ADDITIONALINCOME)
    value_list_work_income.append(value_list)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    text_additionalincome = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_JOB_SOURCE_ADDITIONALINCOME)
    if text_additionalincome != 'отсутствует':
        text_sum_additionalincome = page_mp.random_all(nuber=True, len_srt=5)
        page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_SUM_ADDITIONAL_INCOME, text_sum_additionalincome)
        value_list_work_income.append([text_sum_additionalincome, page_mp.CLIENT_CARD_JOB_SUM_ADDITIONAL_INCOME])
        page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_advance_payment_date = page_mp.random_all(day=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ADVANCE_PAYMENT_DATE, text_advance_payment_date)
    value_list_work_income.append([text_advance_payment_date, page_mp.CLIENT_CARD_JOB_ADVANCE_PAYMENT_DATE])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_job_pyday = page_mp.random_all(day=True)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_PAYDAY, text_job_pyday)
    value_list_work_income.append([text_job_pyday, page_mp.CLIENT_CARD_JOB_PAYDAY])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_current_obligations = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS, text_current_obligations)
    value_list_work_income.append([text_current_obligations, page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_current_obligations_sum = page_mp.random_all(nuber=True, len_srt=4)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS_SUM, text_current_obligations_sum)
    value_list_work_income.append([text_current_obligations_sum, page_mp.CLIENT_CARD_JOB_CURRENT_OBLIGATIONS_SUM])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_alimony_obligations = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS, text_alimony_obligations)
    value_list_work_income.append([text_alimony_obligations, page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_alimony_obligations_sum = page_mp.random_all(nuber=True, len_srt=4)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS_SUM, text_alimony_obligations_sum)
    value_list_work_income.append([text_alimony_obligations_sum, page_mp.CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS_SUM])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_other_expenses = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES, text_other_expenses)
    value_list_work_income.append([text_other_expenses, page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    text_other_expenses_sum = page_mp.random_all(nuber=True, len_srt=4)
    page_mp.clear_and_send_keys(page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES_SUM, text_other_expenses_sum)
    value_list_work_income.append([text_other_expenses_sum, page_mp.CLIENT_CARD_JOB_OTHER_EXPENSES_SUM])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(3)

    # После созранения крточки, открываем ее и проверяем заполенение полей
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.click_element(page_mp.MENU_WORK_AND_INCOME)

    page_mp.checking_field_values_from_list(value_list_work_income)

@pytest.mark.page_contact_persons
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Контактные лица"')
@allure.title('Изменение существующей карточки, страница "Контактные лица"')
def test_changing_on_old_client_contact_persons(mp, enable_notifications):
    """Изменение на вкладке "Контактные лица"  существующего клиента и сохранение"""
    value_list_contact_persons = []
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardContactPersons(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_CONTACT_PERSONS)

    page_mp.click_element(page_mp.MENU_CONTACT_PERSONS)

    page_mp.click_element(page_mp.CONTACT_PERSONS_BUTTON_NEW_CONTACT)

    text_type_connection = page_mp.change_field_with_select(page_mp.CONTACT_PERSONS_NEW_TYPE_CONNECTION, page_mp.TYPE_CONNECTION_LIST)
    value_list_contact_persons.append([text_type_connection[0], page_mp.TYPE_CONNECTION])

    text_FIO = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.CONTACT_PERSONS_NEW_FIO, text_FIO)
    value_list_contact_persons.append([text_FIO, page_mp.FIO])

    text_contact_phone = page_mp.CONTACT_PHONE_NUMBER_TEXT
    page_mp.clear_and_send_keys(page_mp.CONTACT_PERSONS_PHONE_NUMBER, text_contact_phone, phone=True)
    value_list_contact_persons.append([text_contact_phone, page_mp.PHONE_NUMBER])
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    mp.hide_keyboard()

    page_mp.click_element(page_mp.BUTTON_SAVE)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(3)

    # После созранения крточки, открываем ее и проверяем заполенение полей
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_CONTACT_PERSONS)

    page_mp.click_element(page_mp.MENU_CONTACT_PERSONS)

    # Проверка после сохранения
    text_type_connection, text_fio, text_phone_number = page_mp.text_field_contact_persons(value_list_contact_persons)
    numer_contact_persons = page_mp.find_text_on_page(page_mp.CONTACT_PERSONS_ALL, text_fio)
    page_mp.contact_person_details(page_mp.CONTACT_PERSONS_ALL, numer_contact_persons, text_fio)
    page_mp.contact_person_details(page_mp.CONTACT_PERSONS_TYPE_CONNECTION_ALL, numer_contact_persons, text_type_connection)
    page_mp.contact_person_details(page_mp.CONTACT_PERSONS_FIO_ALL, numer_contact_persons, text_phone_number, phone=True)


@pytest.mark.page_inn_snils
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "ИНН/СНИЛС"')
@allure.title('Изменение существующей карточки, страница "ИНН/СНИЛС"')
def test_changing_on_old_client_inn_snils(mp, enable_notifications):
    """Изменение на вкладке "ИНН/СНИЛС"  существующего клиента и сохранение"""
    value_list_inn_snils = []
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardINNSNILS(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_INN_SNILS)

    page_mp.click_element(page_mp.MENU_INN_SNILS)

    page_mp.compare_text_in_field(page_mp.HEADER_INN_SNILS, page_mp.HEADER_INN_SNILS_TEXT)

    value_list_inn = page_mp.fill_field_inn_snils(page_mp.INN_TEXT_FIELD, page_mp.INN_CROSS, page_mp.INN_CLIENT)
    value_list_inn_snils.append(value_list_inn)

    value_list_snils = page_mp.fill_field_inn_snils(page_mp.SNILS_TEXT_FIELD, page_mp.SNILS_CROSS, page_mp.SNILS_CLIENT)
    value_list_inn_snils.append(value_list_snils)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(3)

    # После созранения крточки, открываем ее и проверяем заполенение полей
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_INN_SNILS)

    page_mp.click_element(page_mp.MENU_INN_SNILS)

    page_mp.checking_field_values_from_list(value_list_inn_snils)

@pytest.mark.page_other_documents
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "Другие документы"')
@allure.title('Изменение существующей карточки, страница "Другие документы"')
def test_changing_on_old_client_other_documents(mp, enable_notifications):
    """Изменение на вкладке "Другие документы"  существующего клиента и сохранение"""
    photo_selectors = []
    page_mp = PageLoginMP(mp)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES
    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)
    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_OTHER_DOCUMENTS)
    page_mp.click_element(page_mp.MENU_OTHER_DOCUMENTS)

    page_mp = ClientCardOtherDocuments(mp)

    for name_photo in page_mp.DOCUMENT_TYPS[:12]:
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS_DOC)

        selector_name_photo = page_mp.get_selector_by_text(name_photo)
        photo_selectors.append(selector_name_photo)
        page_mp.click_element(selector_name_photo)

        if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
            page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)

        page_mp.compare_text_in_field(selector_name_photo, name_photo)

        page_mp.click_element(page_mp.MAKE_PHOTO)

    page_mp.click_element(page_mp.SAVE_CLOSE_CLIENT_CARD)
    time.sleep(10)

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_OTHER_DOCUMENTS)

    page_mp.click_element(page_mp.MENU_OTHER_DOCUMENTS)

    for photo_selector in photo_selectors:
        list_number = photo_selectors.index(photo_selector)
        if not page_mp.field_presence_check(photo_selector):
            page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        page_mp.click_element(photo_selector)
        page_mp.compare_text_in_field(page_mp.NAME_DOCUMENT, page_mp.DOCUMENT_TYPS[list_number])
        page_mp.driver.back()

    # name_preview_list = page_mp.scroll_preview_list_documents()
    # page_mp.logger.info(f"page_mp.DOCUMENT_TYPS[:12] = {page_mp.DOCUMENT_TYPS[:12]}")
    # assert sorted(name_preview_list) == sorted(page_mp.DOCUMENT_TYPS[:12])

@pytest.mark.page_asp
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "АСП"')
@allure.title('Добавление АСП, страница "АСП"')
def test_changing_on_old_client_asp(mp, enable_notifications):
    """Добавление АСП """
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp = ClientCardGeneralInformation(mp)
    phone_number = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_MAIN_PHONE)
    phone_number_main = page_mp.editing_phone_number(phone_number)

    page_mp = ClientCardASP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_ASP)

    page_mp.click_element(page_mp.MENU_ASP)

    page_mp.click_element(page_mp.CLIENT_CARD_ASP_CREATE_APPLICATION_ASP)


    names_photos = page_mp.TYPE_ASP
    for name_photo in names_photos:
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
        selector_name_photo = page_mp.get_selector_by_text(name_photo)
        page_mp.click_element(selector_name_photo)

        if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
            page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)

        page_mp.compare_text_in_field(selector_name_photo, name_photo)

        page_mp.click_element(page_mp.MAKE_PHOTO)

    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_ASP_PHONE_NUMBER, phone_number_main)
    page_mp.compare_text_in_field(page_mp.CLIENT_CARD_ASP_STATUS, page_mp.TEXT_ASP_STATUS_IN_WORK)



# @pytest.mark.skip(reason="Найти причину почему не проходит")
@pytest.mark.page_asp
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "АСП"')
@allure.title('Печать согласия об АСП, страница "АСП"')
def test_changing_on_old_client_print_asp(mp, enable_notifications):
    """Печать согласия об АСП, страница 'АСП'"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardASP(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_ASP)

    page_mp.click_element(page_mp.MENU_ASP)

    page_mp.click_element(page_mp.CLIENT_CARD_ASP_PRINT_AGREEMENT_ASP)
    page_mp.click_element(page_mp.CLIENT_CARD_ASP_SIGNATOTY_ASP)

    assert page_mp.search_text_in_page(page_mp.TEXT_ASP_SELECT_SAVE_PDF)

@pytest.mark.page_asp
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('КК Страница "АСП"')
@allure.title('Печать личной карточки , страница "АСП"')
def test_changing_on_old_client_print_asp(mp, enable_notifications):
    """Печать личной карточки, страница 'АСП'"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardASP(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_ASP)

    page_mp.click_element(page_mp.MENU_ASP)

    page_mp.click_element(page_mp.CLIENT_CARD_ASP_PRINT_PERSONAL_CARD)

    assert page_mp.search_text_in_page(page_mp.TEXT_ASP_SELECT_SAVE_PDF)

@pytest.mark.with_parameters
@pytest.mark.page_visit_inspection
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.parametrize("place_of_inspection", [pytest.param('Дом', marks=pytest.mark.sanity), 'Работа'])
@pytest.mark.parametrize("phone_selection", [pytest.param('Основной', marks=pytest.mark.sanity), 'Дополнительный'])
@allure.epic('КК Страница "Визит-осмотры"')
@allure.title('Новый визит-осмотр , страница "Визит-осмотры"')
def test_changing_on_old_client_new_visit_inspection(mp, place_of_inspection, phone_selection, enable_notifications):
    """ Создает новый Вмизит-осмотр, страница 'Визит-осмотры'"""
    # place_of_inspection = 'Дом'
    # phone_selection = 'Основной'
    value_list_visit_inspection = []
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)

    page_mp = ClientCardGeneralInformation(mp)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_OLD_CLIENT_RES

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    phone_main_selector = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_MAIN_PHONE)
    phone_second_selector = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_SECOND_PHONE)

    page_mp.scrolls_all(page_mp.SCROLL_DOWN, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN, scroll_page_selector=page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    if page_mp.find_search_field_two_scrolls(page_mp.CLIENT_CARD_FACT_ADDRESS):
        text_address_home = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_FACT_ADDRESS)
    else:
        text_address_home = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_REGISTRATION_ADDRESS)
    page_mp.logger.info(f"text_address = {text_address_home}")

    page_mp = ClientCardWorkAndIncomeExpenses(mp)
    page_mp.scrolls_all(page_mp.SCROLL_DOWN, scroll_page_selector=page_mp.HEADING_GENERAL_INFORMATION,
                        selector_scroll_to_element=page_mp.MENU_WORK_AND_INCOME)

    page_mp.click_element(page_mp.MENU_WORK_AND_INCOME)
    text_job_address = page_mp.check_text_by_selector(page_mp.CLIENT_CARD_JOB_ADRESS_JOB)
    page_mp.logger.info(f"text_job_address = {text_job_address}")


    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD,
                        selector_scroll_to_element=page_mp.MENU_VESIT_INSPECTIONS)


    page_mp.click_element(page_mp.MENU_VESIT_INSPECTIONS)

    page_mp = ClientCardVisitInspeckion(mp)
    page_mp.click_element(page_mp.VISIT_INSPECTION_ADDRESS, wait_time=80) # ожидание до 80, т.к. очень долго открывается на к15

    if page_mp.field_presence_check(page_mp.VISIT_INSPECTION_BUTTON_CREATE):
        page_mp.click_element(page_mp.VISIT_INSPECTION_BUTTON_CREATE)

    selector_address, text_address = page_mp.check_address_vivit_inspection(text_address_home,
                                                                            text_job_address, place_of_inspection)
    page_mp.click_element(selector_address)
    value_list_visit_inspection.append([text_address, page_mp.VISIT_INSPECTION_ADDRESS])

    page_mp.compare_text_in_field(page_mp.VISIT_INSPECTION_PHONE, phone_main_selector, phone=True)
    text_phone = page_mp.check_phone_vivit_inspection(phone_selection, phone_main_selector, phone_second_selector)
    page_mp.compare_text_in_field(page_mp.VISIT_INSPECTION_PHONE, text_phone, phone=True)
    value_list_visit_inspection.append([text_phone, page_mp.VISIT_INSPECTION_PHONE])

    text_comment = page_mp.random_all(str_cyrillic=True, len_srt=10)
    page_mp.clear_and_send_keys(page_mp.VISIT_INSPECTION_COMMENT, text_comment)
    value_list_visit_inspection.append([text_comment, page_mp.VISIT_INSPECTION_COMMENT])

    page_mp.add_photo_visit_inspection(place_of_inspection)

    page_mp.click_element(page_mp.VISIT_INSPECTION_GEOPOZITION)
    if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
        page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)
    page_mp.field_presence_check(page_mp.VISIT_INSPECTION_GEOPOZITION_TEXT_IN_PHOTO, wait_time=0.5)
    page_mp.click_element(page_mp.SELECT_PHOTO_FROM_DEVICES)

    elements_photo = page_mp.search_all_elements(page_mp.PHOHO_ALL_GALLERY)
    page_mp.click_element(elements_photo[page_mp.PHOTO_GEOPOZITION])
    # page_mp.click_element(page_mp.PHOTO_IN_GALLERY)

    time.sleep(2)
