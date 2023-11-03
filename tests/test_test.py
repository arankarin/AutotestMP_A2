import time

import pytest
import allure

from page_objects.ClientSearch import ClientSearch
from page_objects.ClientCardGeneralInformation import ClientCardGeneralInformation
from page_objects.ClientCardDocuments import ClientCardDocuments
from page_objects.ClientCardWorkAndIncomeExpenses import ClientCardWorkAndIncomeExpenses
from page_objects.ClientCardContactPersons import ClientCardContactPersons
from page_objects.ClientCardINNSNILS import ClientCardINNSNILS
from page_objects.ClientCardClientAddress import ClientCardClientAddress

# @pytest.mark.skip(reason="Тест для теста")
# @pytest.mark.single_run
# @pytest.mark.regression
# @pytest.mark.sanity
# @pytest.mark.parametrize("citizenship_list", [['РОССИЯ', 'Тестфамилия', 'Росиия', 'Тестотчество', '01012000', '79310000013']])
# @pytest.mark.parametrize("recognize_photo", [True])
# @allure.epic("Основной Функционал")
# @allure.title('Создание и сохранение нового клиента')
# def test_save_new_client_test(mp, citizenship_list, recognize_photo, enable_notifications):
#     """Создать нового клиента на К15 с данными из метода customer_search_all_fields
#     Заполнить все обязательные поля и сохранить"""
#     page_mp = ClientSearch(mp)
#     if recognize_photo and citizenship_list != ['РОССИЯ', 'Тестфамилия', 'Росиия', 'Тестотчество', '01012000', '79310000013']:
#         pytest.skip('Пропускаем, т.к. не реализован функцинал')
#     page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
#     page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
#     page_mp.click_element(page_mp.MENU_ADD)
#
#     citizenship = citizenship_list[0]
#     surname_text = citizenship_list[1]
#     name_text = citizenship_list[2]
#     # patronymic_textviev_parent_text = citizenship_list[3]
#     patronymic_textviev_parent_text = page_mp.random_all(patronymic=True, len_srt=4)
#     date_of_birth_text = citizenship_list[4]
#     # phone_number_text = citizenship_list[5]
#     phone_number_text = page_mp.random_all(phone=True)
#     fio_text = surname_text + ' ' +  name_text + ' ' + patronymic_textviev_parent_text
#     fio_text_down = fio_text.lower()
#
#     # Заполение полей тестовыми данными на странице "Найти клиента"
#     page_mp.clear_and_send_keys(page_mp.CLIENT_SURNAME, surname_text)
#     page_mp.clear_and_send_keys(page_mp.CLIENT_NAME, name_text)
#     page_mp.clear_and_send_keys(page_mp.PATRONYMIC_TEXTVIEV_PARENT, patronymic_textviev_parent_text)
#     page_mp.clear_and_send_keys(page_mp.DATE_OF_BIRTH_TEXTVIEV_PARENT, date_of_birth_text, date=True)
#     page_mp.clear_and_send_keys(page_mp.PHONE_NUMBER_TEXTVIEV_PARENT, phone_number_text, phone=True)
#     page_mp.click_element(page_mp.FIND_CLIENT_BUTTON_PARENT)
#
#     # Вкладка Общая информация
#     page_mp = ClientCardGeneralInformation(mp)
#     citizenship_selector = page_mp.CITIZENSHIP_DICT[citizenship]
#     page_mp.text_field_new_client(page_mp.CLIENT_CARD_CITIZENSHIP)
#     page_mp.click_element(page_mp.CLIENT_CARD_CITIZENSHIP)
#     page_mp.click_element(citizenship_selector)
#     page_mp.click_element(page_mp.CANCEL_BUTTUN)
#
#     page_mp.click_element(page_mp.MENU_DOCUMENTS)
#
#     # Вкладка Документы
#     page_mp = ClientCardDocuments(mp)
#     if citizenship == 'РОССИЯ':
#         page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
#         page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT_RF)
#     else:
#         page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC)
#         page_mp.click_element(page_mp.CLIENT_CARD_DOC_TYPE_MAIN_DOC_PASPORT)
#
#     page_mp.scrolls_all(page_mp.SCROLL_DOWN, selector_scroll_to_element=page_mp.BUTTON_ADD_PHOTOS)
#
#     page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)
#     selector_name_photo = page_mp.get_selector_by_text(page_mp.DOCUMENT_TYPS_RUSSIA[1])
#     page_mp.click_element(selector_name_photo)
#
#     if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
#         page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)
#     page_mp.click_element(page_mp.SELECT_PHOTO_FROM_DEVICES)
#     el_1 = page_mp.search_element(page_mp.PHOTO_IN_GALLERY)
#     page_mp.logger.info(f"Поиск элемента методом presence_of_element_located по селектору фото, по Id, результат= {el_1}")
#     page_mp.click_element(page_mp.PHOTO_IN_GALLERY)
#     time.sleep(4)
