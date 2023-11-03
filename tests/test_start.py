import time
import allure
import pytest

from page_objects.MainPages import MainPage
from page_objects.ClientSearch import ClientSearch
from page_objects.PageLoginMP import PageLoginMP

@pytest.mark.desktop
@pytest.mark.sanity
@allure.epic('Страница "Рабочий стол"')
@allure.title('Проверка наличия всех пунктов меню')
def test_main_menu(mp, enable_notifications):
    """Тест наличия всех пунктов меню на гланой странице"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
    page_mp.field_presence_check(page_mp.MAIN_PAGE)
    page_mp.main_menu()

@pytest.mark.desktop
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('Страница "Рабочий стол"')
@allure.title('Проверка работы меню на главной странице')
def test_menu_click(mp, enable_notifications):
    """Проверка переходов по всем пунктам меню, пункты задаются параметрами"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_K15, page_mp.PASSWORD_VOROBEV)
    # time.sleep(2)
    #'Мои клиенты':
    page_mp.click_element(page_mp.MENU_MY_CLIENTS)
    page_mp.field_presence_check(page_mp.MY_CLIENTS_MENU_ALL)
    page_mp.field_presence_check(page_mp.MENU_MY_CLIENTS)
    mp.back()
    # 'Добавить':
    page_mp.click_element(page_mp.MENU_ADD)
    page_mp.field_presence_check(page_mp.PAGE_CREATION_CLIENT)
    page_mp = ClientSearch(mp)
    page_mp.field_presence_check(page_mp.PHONE_NUMBER_TEXTVIEV_PARENT)
    page_mp = MainPage(mp)
    mp.back()
    #'Последние события':
    page_mp.click_element(page_mp.LATEST_EVENTS_TEXT)
    page_mp.field_presence_check(page_mp.LATEST_EVENTS_TEXT)
    page_mp.field_presence_check(page_mp.BUTTON_CLOSE)
    mp.back()
    #'Мои клиенты':
    page_mp.click_element(page_mp.MENU_MY_APPLICATIONS)
    page_mp.field_presence_check(page_mp.MENU_MY_APPLICATIONS)
    page_mp.field_presence_check(page_mp.MENU_MY_APPLICATIONS_REFINEMENT)
    mp.back()
    #'Онлайн заявки':
    page_mp.click_element(page_mp.MENU_ONLINE_APPLICATIONS)
    page_mp.field_presence_check(page_mp.MENU_ONLINE_APPLICATIONS)
    page_mp.field_presence_check(page_mp.MENU_ONLINE_APPLICATIONS_INCOMING_APPLICATIONS)
    mp.back()
    #'Монитор должников':
    page_mp.click_element(page_mp.MENU_DETOP_MONITOR)
    page_mp.field_presence_check(page_mp.MENU_DETOP_MONITOR)
    page_mp.field_presence_check(page_mp.TOTAL)
    mp.back()
    'Мои отчеты'
    page_mp.click_element(page_mp.MENU_MY_REPORTS)
    time.sleep(2)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_TODAY)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_BIRTHDAYS)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_PLANNED_REPAYMENTS)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_UNDELIVERED_ORIGINAL_ASP)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_ISSUED_LOANS)
    #'Оплатили сегодня'
    page_mp.click_element(page_mp.MENU_MY_REPORTS_PAID_TODAY)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_TODAY)
    page_mp.field_presence_check(page_mp.TOTAL)
    mp.back()
    # Дни рождения
    page_mp.click_element(page_mp.MENU_MY_REPORTS_PAID_BIRTHDAYS)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_BIRTHDAYS)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_BIRTHDAYS_ACTIV)
    mp.back()
    # Планируемые погашения
    page_mp.click_element(page_mp.MENU_MY_REPORTS_PAID_PLANNED_REPAYMENTS)
    page_mp.field_presence_check(page_mp.TOTAL)
    mp.back()
    # Планируемые погашения
    page_mp.click_element(page_mp.MENU_MY_REPORTS_PAID_UNDELIVERED_ORIGINAL_ASP)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_UNDELIVERED_ORIGINAL_ASP)
    mp.back()
    #
    page_mp.click_element(page_mp.MENU_MY_REPORTS_PAID_ISSUED_LOANS)
    page_mp.field_presence_check(page_mp.MENU_MY_REPORTS_PAID_ISSUED_LOANS)
    mp.back()
    # Мои показатели
    page_mp.click_element(page_mp.MENU_MY_PERFOMANCE)
    page_mp.field_presence_check(page_mp.MENU_MY_PERFOMANCE)
    page_mp.field_presence_check(page_mp.MENU_MY_PERFOMANCE_CURRENTPERIOD)
    mp.back()
    page_mp.click_element(page_mp.MENU_MY_REPORTS)
    # Калькулятор займов
    page_mp.click_element(page_mp.MENU_LOAN_CALCULATOR)
    page_mp.field_presence_check(page_mp.MENU_LOAN_CALCULATOR)
    page_mp.field_presence_check(page_mp.MENU_LOAN_CALCULATOR_DATE_OF_1_PAYMENT)
    mp.back()
    page_mp.scrolls_all(page_mp.SCROLL_DOWN)
    # Настройки
    page_mp.click_element(page_mp.MENU_SETTINGS)
    page_mp.field_presence_check(page_mp.MENU_SETTINGS)
    page_mp.field_presence_check(page_mp.MENU_SETTINGS_ALLOW_LINE_SWIPE)
    mp.back()


    # for element_menu in page_mp.MAIN_MENU:
        # if element_menu == 'Мои отчеты':
        #     page_mp.open_menu(element_menu)
        #     res = page_mp.check_text("Оплатили сегодня ")
        #     assert res == "Оплатили сегодня "
        #     page_mp.open_menu(element_menu)
        #     page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        # elif element_menu == 'Добавить':
        #     page_mp.open_menu(element_menu)
        #     res = page_mp.check_text("Поиск клиента")
        #     assert res == "Поиск клиента"
        #     page_mp.button_click(page_mp.BUTTON_BACK)
        # elif element_menu == 'Онлайн заявки':
        #     page_mp.open_menu(element_menu)
        #     res = page_mp.check_text("Онлайн-заявки")
        #     assert res == "Онлайн-заявки"
        #     page_mp.button_click(page_mp.BUTTON_BACK)
        # elif element_menu == 'Последние события':
        #     page_mp.open_menu(element_menu)
        #     assert page_mp.field_presence_check(page_mp.TEXT_LATEST_EVENTS)
        #     page_mp.button_click(page_mp.BUTTON_CLOSE)
        # else:
        #     if element_menu == 'Калькулятор займов':
        #         page_mp.scrolls_all(page_mp.SCROLL_DOWN)
        #     page_mp.open_menu(element_menu)
        #     text_page = page_mp.check_text(element_menu)
        #     assert text_page == element_menu
        #     page_mp.button_click(page_mp.BUTTON_BACK)

# @pytest.mark.skip(reason="Проверку будем делать когда демо починят")
@pytest.mark.desktop
@pytest.mark.regression
@pytest.mark.sanity
@allure.epic('Страница "Рабочий стол"')
@allure.title('Проверка количества клиентов')
def test_total_clients(mp, enable_notifications):
    """Количество клиентов, проверка производится на на рабочей у Воробьева 160 клиента"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.login_km(page_mp.TB_BAIBOL_DEMO, page_mp.PASSWORD_VOROBEV)
    time.sleep(6) # Тольк на демо
    total_clients = page_mp.compare_text_in_field(page_mp.TOTAL_CLIENTS, page_mp.TOTAL_CLIENTS_TORBO)

@pytest.mark.page_about_program
@pytest.mark.smoke
@allure.epic("Страница 'О программе'")
@allure.title('Переключение на демо базу')
def test_base_change(mp, enable_notifications):
    """Переключение на демо базу"""
    page_mp = PageLoginMP(mp)
    page_mp.scrolls_all(page_mp.SCROLL_PUSH_NOTIFICATIONS)
    page_mp.base_change(page_mp.TB_BAIBOL_DEMO)

