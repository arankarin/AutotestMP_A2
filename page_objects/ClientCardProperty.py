import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.MainPages import MainPage


class ClientCardProperty(MainPage):

    BRAND_TS = (By.XPATH, '//android.widget.TextView[@content-desc="Марка ТС"]')
    CAR_NUMBER = (By.XPATH, '//android.widget.TextView[@content-desc="Номер ТС"]')
    WIN_TS = (By.XPATH, '//android.widget.TextView[@content-desc="WIN ТС"]')
    YEAR_OF_RELEASE_CAR = (By.XPATH, '//android.widget.TextView[@content-desc="Год выпуска ТС"]')
    CAR_BODY_COLOR = (By.XPATH, '//android.widget.TextView[@content-desc="Цвет кузова ТС"]')
    SEND_PHOTO = (By.XPATH, '//android.view.View[@content-desc="Отправить фото"]')

    TS_DOCUMENT_TYPS = ['Акт осмотра залога', 'ПТС (Страница 1)', 'ПТС (Страница 2)', 'СТС (Страница 1)', 'СТС (Страница 2)',
                        'Фото - багажный отсек', 'Фото - вид ветрового стекла изнутри', 'Фото - вид ветрового стекла снаружи',
                        'Фото - вид сверху крыша', 'Вид сзади', 'Вид спереди', 'Фото - вид сзади под углом 45',
                        'Вид слева при закрытых дверях', 'Фото - вид слева при открых дверях', 'Вид справа при закрытых дверях',
                        'Фото - вид спереди под углом 45', 'Фото - вид справа при открытых дверях', 'Фото - диски и шины',
                        'Фото - другое', 'Фото - моторный отсек', 'Фото - панель приборов', 'Фото - показания спидометров',
                        'Фото - пороги', 'Салон', 'Фото - салон (потолок)', 'Фото - салон (сиденья)', 'Фото стойки']

    # Данные ТС у "Аспемова Ивана Михайловна" на ДЕМО
    BRAND_TS_TEXT = 'Lifan'
    CAR_NUMBER_TEXT = 'О111СО178'
    WIN_TS_TEXT = 'JMZBK14F261303458'
    YEAR_OF_RELEASE_CAR_TEXT = '2021'
    CAR_BODY_COLOR_TEXT = 'белый'
