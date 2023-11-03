from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardASP(MainPage):

    CLIENT_CARD_ASP_CREATE_APPLICATION_ASP = (By.XPATH, '//android.view.View[@content-desc="Создать заявку на АСП"]')
    CLIENT_CARD_ASP_PRINT_AGREEMENT_ASP = (By.XPATH, '//android.view.View[@content-desc="Печать согл. об АСП"]')
    CLIENT_CARD_ASP_PRINT_PERSONAL_CARD = (By.XPATH, '//android.view.View[@content-desc="Печать личной карточки"]')
    CLIENT_CARD_ASP_NEXT = (By.XPATH, '//android.view.View[@content-desc="Кнопка Далее в АСП"]')
    CLIENT_CARD_ASP_PHONE_NUMBER = (By.XPATH, '//android.widget.TextView[@content-desc="Номер телефона АСП"]')
    CLIENT_CARD_ASP_STATUS = (By.XPATH, '//android.widget.TextView[@content-desc="Статус АСП"]')
    CLIENT_CARD_ASP_SIGNATOTY_ASP = (By.XPATH, '//android.widget.TextView[@content-desc="Торбо Ольга Михайловна"]')
    CLIENT_CARD_ASP_SELECT_PRINTER = (By.ID, 'com.android.printspooler:id/destination_spinner')


    TEXT_ASP_STATUS_IN_WORK = 'В работе'
    TEXT_ASP_SELECT_PRINTER = 'Выберите принтер'
    TEXT_ASP_SELECT_SAVE_PDF = 'Сохранить как PDF'


    TYPE_ASP = ['Соглашение об АСП 1 стр', 'Соглашение об АСП 2 стр', 'Фото с паспортом', 'Фото с соглашением']





