from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardApplicationsAndContracts(MainPage):

    #Заявки и договоры селекторы
    BUTTON_NEW_CONTRACT = (By.XPATH, '//android.view.View[@content-desc="Кнопка Новая заявка"]')
    BUTTON_CREATE_LOAN_APPLICATION = (By.XPATH, '//android.view.View[@content-desc="Кнопка Создать заявку на займ"]')
    BUTTON_LINK_PERSONAL_ACCOUNT = (By.XPATH, '//android.view.View[@content-desc="Кнопка Отправить ссылку на личный кабинет"]')

    # Вкладка Завки и договоры для создания заявки, поле нажатия на "Новая заявка"
    APPLICATIONS_AND_CONTRACTS_DIRECTION_LOAN_EXPENDITURE = (By.XPATH, '//android.widget.TextView[@content-desc="Направление расходования займа:"]')
    DIRECTION_LOAN_EXPENDITURE_PERSONAL_TARGET = (By.XPATH, '//android.widget.TextView[@content-desc="Личные цели"]')
    VIEW_CONTRACTS_IVDIVIDUAL1 = (By.XPATH, '//android.widget.TextView[@content-desc="Индивидуальный-1"]')
    DESIRED_DAY_PAYMENT = (By.XPATH, '//android.view.View[@content-desc="Поле Желаемый день ежемесячного платежа"]/..')
    TEXT_DESIRED_DAY_PAYMENT = '10'
    LOAN_TERM = (By.XPATH, '//android.view.View[@content-desc="Поле Срок займа"]/..')
    TEXT_LOAN_TERM = '7'
    SUMM_CONTRACT = (By.XPATH, '//android.view.View[@content-desc="Поле Сумма займа"]/..')
    TEXT_SUMM_CONTRACT = '20000'

