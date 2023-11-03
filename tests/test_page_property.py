import time
import pytest
import allure

from page_objects.ClientCardProperty import ClientCardProperty
from page_objects.ClientCardOtherDocuments import ClientCardOtherDocuments
from page_objects.PageLoginMP import PageLoginMP


@pytest.mark.page_property
@allure.epic('КК Страница "Имущество"')
@allure.title('Проверка данных по ТС, страница "Имущество"')
def test_field_check_property(mp, enable_notifications):
    """Проверка данных по ТС, страница 'Имущество'"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_DEMO, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PROPERTY_DEMO
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PROPERTY_RES_DEMO

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_PROPERTY)

    page_mp.click_element(page_mp.MENU_PROPERTY)

    page_mp = ClientCardProperty(mp)

    page_mp.compare_text_in_field(page_mp.BRAND_TS, page_mp.BRAND_TS_TEXT)
    page_mp.compare_text_in_field(page_mp.CAR_NUMBER, page_mp.CAR_NUMBER_TEXT)
    page_mp.click_element(page_mp.CAR_NUMBER)
    page_mp.compare_text_in_field(page_mp.WIN_TS, page_mp.WIN_TS_TEXT)
    page_mp.compare_text_in_field(page_mp.YEAR_OF_RELEASE_CAR, page_mp.YEAR_OF_RELEASE_CAR_TEXT)
    page_mp.compare_text_in_field(page_mp.CAR_BODY_COLOR, page_mp.CAR_BODY_COLOR_TEXT)

@pytest.mark.page_property
@allure.epic('КК Страница "Имущество"')
@allure.title('Добавление фото ТС, страница "Имущество"')
def test_property_photo(mp, enable_notifications):
    """Добавление фото ТС, страница 'Имущество' (Проверяем 5 фото)"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_DEMO, page_mp.PASSWORD_VOROBEV)

    text_for_search_old_client = page_mp.TEXT_FOR_SEARCH_CLIENT_PROPERTY_DEMO
    text_for_search_old_client_res = page_mp.TEXT_FOR_SEARCH_CLIENT_PROPERTY_RES_DEMO

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_PROPERTY)

    page_mp.click_element(page_mp.MENU_PROPERTY)

    page_mp = ClientCardProperty(mp)

    for name_photo in page_mp.TS_DOCUMENT_TYPS[:5]:
        page_mp.click_element(page_mp.BUTTON_ADD_PHOTOS)

        selector_name_photo = page_mp.get_selector_by_text(name_photo)
        page_mp.click_element(selector_name_photo)

        if page_mp.field_presence_check(page_mp.CAMERA_PERMISSION_BUTTON):
            page_mp.click_element(page_mp.CAMERA_PERMISSION_BUTTON)

        page_mp.compare_text_in_field(selector_name_photo, name_photo)

        page_mp.click_element(page_mp.MAKE_PHOTO)

    page_mp.click_element(page_mp.SEND_PHOTO)
    time.sleep(3)

    page_mp.click_element(page_mp.BUTTON_BACK)
    page_mp.click_element(page_mp.BUTTON_BACK)

    page_mp.open_old_client(text_for_search_old_client, text_for_search_old_client_res)

    page_mp.scrolls_all(page_mp.SCROLL_RIGHT_MENU_CLIENT_CARD, scroll_page_selector=page_mp.CLIENT_CARD_SURNAME,
                        selector_scroll_to_element=page_mp.MENU_PROPERTY)

    page_mp.click_element(page_mp.MENU_PROPERTY)

    page_mp = ClientCardOtherDocuments(mp)
    name_preview_list = page_mp.scroll_preview_list_documents()
    page_mp = ClientCardProperty(mp)
    page_mp.logger.info(f"page_mp.TS_DOCUMENT_TYPS[:5] = {page_mp.TS_DOCUMENT_TYPS[:5]}")
    assert sorted(name_preview_list) == sorted(page_mp.TS_DOCUMENT_TYPS[:5])