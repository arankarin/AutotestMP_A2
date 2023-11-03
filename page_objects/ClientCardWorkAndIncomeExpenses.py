from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardWorkAndIncomeExpenses(MainPage):

    # Работа и Доходы/расходы Селекторы
    CLIENT_CARD_JOB_ADRESS_JOB = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес работы"]')
    CLIENT_CARD_JOB_CATEGORY_POZITION = (By.XPATH, '//android.widget.TextView[@content-desc="Категория должности:"]')
    CLIENT_CARD_JOB_POZITION = (By.XPATH, '//android.view.View[@content-desc="Должность"]/..')
    CLIENT_CARD_JOB_PLACE_MAIN_INCOME = (By.XPATH, '//android.view.View[@content-desc="Место основного дохода"]/..')
    CLIENT_CARD_JOB_SUM_MAIN_INCOME = (By.XPATH, '//android.view.View[@content-desc="Сумма основного дохода"]/..')
    CLIENT_CARD_JOB_EXPERIENCE = (By.XPATH, '//android.view.View[@content-desc="Стаж на последнем месте работы"]/..')
    CLIENT_CARD_JOB_SOURCE_ADDITIONALINCOME = (By.XPATH, '//android.widget.TextView[@content-desc="Источник дополнительного дохода:"]')
    CLIENT_CARD_JOB_SUM_ADDITIONAL_INCOME = (By.XPATH, '//android.view.View[@content-desc="Сумма дополнительного дохода"]/..')
    CLIENT_CARD_JOB_ADVANCE_PAYMENT_DATE = (By.XPATH, '//android.view.View[@content-desc="Дата аванса"]/..')
    CLIENT_CARD_JOB_PAYDAY = (By.XPATH, '//android.view.View[@content-desc="Дата зарплаты"]/..')
    CLIENT_CARD_JOB_CURRENT_OBLIGATIONS = (By.XPATH, '//android.view.View[@content-desc="Текущие обязательства"]/..')
    CLIENT_CARD_JOB_CURRENT_OBLIGATIONS_SUM = (By.XPATH, '//android.view.View[@content-desc="Сумма текущих обязательств"]/..')
    CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS = (By.XPATH, '//android.view.View[@content-desc="Алиментные обязательства"]/..')
    CLIENT_CARD_JOB_ALIMONY_OBLIGATIONS_SUM = (By.XPATH, '//android.view.View[@content-desc="Сумма алиментных обязательств"]/..')
    CLIENT_CARD_JOB_OTHER_EXPENSES = (By.XPATH, '//android.view.View[@content-desc="Прочие расходы"]/..')
    CLIENT_CARD_JOB_OTHER_EXPENSES_SUM = (By.XPATH, '//android.view.View[@content-desc="Сумма прочих расходов"]/..')
    CLIENT_CARD_JOB_BUTTON_BANC_CARD = (By.XPATH, '//android.view.View[@content-desc="Банковские карты"]')

    # Вкладка Работа и Доходы/расходы заполение нового клиента
    CATEGORY_POZITION_STREET_SWEEPER = (By.XPATH, '//android.widget.TextView[@content-desc="Дворник"]')
    POZITION_TEXT = 'Дворник'
    PLACE_MAIN_INCOME_TEXT = 'ООО РАБОТА'
    SUM_MAIN_INCOME_TEXT = '110000'
    EXPERIENCE_TEXT = '6'
    SOURCE_ADDITIONALINCOME_PART_TIME_JOB = (By.XPATH, '//android.widget.TextView[@content-desc="постоянная подработка в другой организации"]')
    SUM_ADDITIONAL_INCOME_TEXT = '10000'
    ADVANCE_PAYMENT_DATE_TEXT = '20'
    PAYDAY_TEXT = '5'
    CURRENT_OBLIGATIONS_TEXT = 'Обязательства текущие'
    CURRENT_OBLIGATIONS_SUM_TEXT = '1000'
    ALIMONY_OBLIGATIONS_TEXT = 'Обязательства алиментные'
    ALIMONY_OBLIGATIONS_SUM_TEXT = '1100'
    OTHER_EXPENSES_TEXT = 'Расходы прочие'
    OTHER_EXPENSES_SUM_TEXT = '15000'

    CATEGORY_POZITION = ['Не выбрано', 'бригадир', 'водитель', 'Водитель грузового ТС', 'Водитель легкового ТС',
                         'Водитель спец. техники', 'Государственные служащие высоких чинов', 'Государственный служащий',
                         'грузчик', 'дворник', 'домохозяйка', 'другое', 'кассир', 'комплектовщик', 'Кондуктор',
                         'Консьерж', 'маляр', 'Мастер маникюра/педикюра', 'мойщик', 'Мойщик(ца) посуды',
                         'монтажник', 'нет', 'Нянька/сиделка', 'оператор', 'официант', 'Парикмахер', 'Пенсионер',
                         'Перекупщик (без ИП/ООО)', 'повар', 'подсобный рабочий', 'Правительство РФ', 'Преподаватель',
                         'продавец', 'Прочее', 'рабочий', 'разнорабочий', 'Садовник', 'слесарь', 'Сотрудник счетной палаты',
                         'строитель', 'Судебная власть, права человека', 'Таксист', 'техник', 'Тренер', 'уборщик/уборщица',
                         'фасовщик', 'Фасовщик/упаковщик', 'Флорист', 'Центральная избирательная комиссия', 'Шиномонтажник',
                         'электрик', 'Юрист']

    SOURCE_ADDITIONALINCOME = ['Не выбрано', 'отсутствует', 'постоянная подработка в другой организации',
                               'средства от подработки в такси, грузоперевозки',
                               'средства от сдачи в аренду квартиры, комнаты',
                               'средства, полученные от работ на срубах, стройке домов, дач',
                               'средства, полученные от ухода за больными, ухода за детьми']