import time
import pytest
import allure

from page_objects.PageLoginMP import PageLoginMP

@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка Верного ввода пароля')
def test_check_positive_password(mp, enable_notifications):
    """Проверка Верного ввода пароля"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
    assert page_mp.field_presence_check(page_mp.MAIN_PAGE)

@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка НЕверного ввода пароля')
def test_check_negative_password(mp, enable_notifications):
    """Проверка НЕверного ввода пароля"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV_NEGATIVE)
    assert page_mp.field_presence_check(page_mp.ERROR_INCORRECT_PASSWORD)


@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка ФИО КМ')
def test_check_fio(mp, enable_notifications):
    """Проверка ФИО КМ"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_K15)
    fio_km = page_mp.FIO_KM_TEXT
    page_mp.compare_text_in_field(page_mp.FIO_KM, fio_km)

# Спараску убрали с страницы ввода пароля
# @pytest.mark.page_login_mp
# @allure.epic('Страница входа в МП')
# @allure.title('Проверка Спрака по приложению')
# def test_check_help_about_program(mp, enable_notifications):
#     """Проверка Спрака по приложению"""
#     page_mp = PageLoginMP(mp)
#     page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
#     page_mp.base_change(page_mp.TB_BAIBOL_K15)
#     page_mp.click_element(page_mp.HELP_ABOUT_PROGRAM)
#     assert page_mp.field_presence_check(page_mp.HELP_ABOUT_PROGRAM_TITLE)

@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка О программе')
def test_check_about_program(mp, enable_notifications):
    """Проверка О программе"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_K15)
    page_mp.click_element(page_mp.VERSION_MP)
    assert page_mp.field_presence_check(page_mp.ABOUT_PROGRAM)

@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка Версии МП')
def test_check_version_mp(mp, enable_notifications):
    """Проверка Версии МП"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_K15)
    page_mp.compare_text_in_field(page_mp.VERSION_MP, page_mp.VERSION_MP_TEXT)

@pytest.mark.skip(reason="Пока не придумаем, как получить сервер недоступен, тест был проверен, когда база не работала")
@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка "Ошибка при обращении к серверу"')
def test_check_error_accessign_server(mp, enable_notifications):
    """Проверка 'Ошибка при обращении к серверу'
    Если подключения к серверу НЕТ и на экране текст ошибки, тест проходит успешно"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_DEMO)
    assert page_mp.field_presence_check(page_mp.ERROR_ACCESSING_SERVER)

@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка "Доступ запрещен"')
def test_check_error_access_denoded(mp, enable_notifications):
    """Проверка Доступ запрещен
    Если Доступ запрещен и на экране текст ошибки, тест проходит успешно"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    assert page_mp.field_presence_check(page_mp.ACCESS_IS_DENIED)


@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка нажатия. Перебор всех цифр')
def test_iterate_all_numbers_password(mp, enable_notifications):
    """Проверка нажатия. Перебор всех цифр"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_K15)
    page_mp.iterate_all_numbers()


@pytest.mark.page_login_mp
@allure.epic('Страница входа в МП')
@allure.title('Проверка удаления. Удаляем все цифры')
def test_select_and_delete_numbers(mp, enable_notifications):
    """Проверка удаления. Удаляем все цыфры"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_K15)
    page_mp.select_and_delete_numbers()
