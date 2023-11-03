from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardGeneralInformation(MainPage):

    # Общая информация селекторы
    # CLIENT_CARD_SURNAME = (By.XPATH, '//android.widget.TextView[@content-desc="Фамилия в карточке клиента"]')
    CLIENT_CARD_NAME = (By.XPATH, '//android.widget.TextView[@content-desc="Имя в карточке клиента"]')
    CLIENT_CARD_PATRONYMIC = (By.XPATH, '//android.widget.TextView[@content-desc="Отчество в карточке клиента"]')
    CLIENT_CARD_MAIN_PHONE = (By.XPATH, '//android.widget.EditText[@content-desc="Основной номер"]')
    CLIENT_CARD_SECOND_PHONE = (By.XPATH, '//android.widget.EditText[@content-desc="Дополнительный номер"]')
    CLIENT_CARD_BIRTHDAY = (By.XPATH, '//android.widget.TextView[@content-desc="Дата рождения в карточке клиента"]')
    CLIENT_CARD_CITIZENSHIP = (By.XPATH, '//android.widget.TextView[@content-desc="Гражданство:"]')
    CLIENT_CARD_GENDER = (By.XPATH, '//android.widget.TextView[@content-desc="Пол"]')
    CLIENT_CARD_FAMILY = (By.XPATH, '//android.widget.TextView[@content-desc="Семейное положение:"]')
    CLIENT_CARD_EDUCATION = (By.XPATH, '//android.widget.TextView[@content-desc="Образование:"]')
    CLIENT_CARD_FOUND_THROUGHT = (By.XPATH, '//android.widget.TextView[@content-desc="О нас узнали через:"]')
    CLIENT_CARD_EMAIL = (By.XPATH, '//android.view.View[@content-desc="Почта"]/..')
    CLIENT_CARD_EMAIL_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Почта валидация"]')
    CLIENT_CARD_REGISTRATION_ADDRESS = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес регистрации проживания"]')
    CLIENT_CARD_FACT_ADDRESS = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес проживания"]')
    # CLIENT_CARD_ADDRESS_FACKT = (By.XPATH, '//android.widget.TextView[@content-desc="Адрес проживания"]')
    CLIENT_CARD_OLD_LOAN = (By.XPATH, '//android.view.View[@content-desc="Предыдущие займы"]/..')
    CLIENT_CARD_OLD_LOAN_VALIDATION = (By.XPATH, '//android.widget.TextView[@content-desc="Предыдущие займы валидация"]')
    BUTTON_COMMENT = (By.XPATH, '//android.view.View[@content-desc="Комментарий"]')

    # Вкладка Общая информация заполение нового клиента
    CLIENT_CARD_CITIZENSHIP_TAJIKISTAN = (By.XPATH, '//android.widget.TextView[@content-desc="ТАДЖИКИСТАН"]')
    CLIENT_CARD_GENDER_MALE = (By.XPATH, '//android.widget.TextView[@content-desc="Мужской"]')
    CLIENT_CARD_FAMILY_STATUS_OFFICIAL_MARRIAGE = (By.XPATH, '//android.widget.TextView[@content-desc="Официальный брак"]')
    CLIENT_CARD_EDUCATION_SECONDARY_TECHNICAL = (By.XPATH, '//android.widget.TextView[@content-desc="Средне техническое"]')
    CLIENT_CARD_LEARNED_THROUGH_FRIENDS = (By.XPATH, '//android.widget.TextView[@content-desc="Знакомые"]')
    EMAIL_TEXT = 'email_test@test.com'
    OLD_LOAN_TEXT = 'нет'
    CITIZENSHIP_DICT = {'КИРГИЗИЯ': (By.XPATH, '//android.widget.TextView[@content-desc="КИРГИЗИЯ"]'),
                        'РОССИЯ': (By.XPATH, '//android.widget.TextView[@content-desc="РОССИЯ"]'),
                        'ТАДЖИКИСТАН': (By.XPATH, '//android.widget.TextView[@content-desc="ТАДЖИКИСТАН"]'),
                        'УЗБЕКИСТАН': (By.XPATH, '//android.widget.TextView[@content-desc="УЗБЕКИСТАН"]')}

    # Гражданство, список
    CITIZENSHIP = ["Не выбрано", "КИРГИЗИЯ", "РОССИЯ", "ТАДЖИКИСТАН", "УЗБЕКИСТАН"]
    # Пол, список
    GENDER = ['Не выбрано', 'Женский', 'Мужской']
    # Семейное полодение список
    FAMILY = ['Не выбрано', 'Гражданский брак', 'Официальный брак', 'Разведенные', 'Холост']
    # Образование список
    EDUCATION = ['Не выбрано', 'Высшее', 'Неполное среднее', 'Несколько высших', 'Средне техническое', 'Среднее',
                 'Ученая степень']
    # Узнали о нас список
    FOUND_THROUGHT = ['Не выбрано', 'Baibol.ru', 'Facebook', 'Instagram', 'Ok.ru', 'SMS', 'Telegram', 'WhatsApp',
                      'Акция', 'Знакомые', 'Интернет (Яндекс, Google)', 'Листовка/визитка', 'Реклама в транспорте',
                      'Рекламные источники', 'Сотрудник Байбол']

    def random_email(self):
        random_str = self.random_all(str_latin=True, len_srt=5)
        return random_str + '@mail.ru'

    def text_field_new_client(self, selector):
        text = self.check_text_by_selector(selector)
        if text == 'Не выбрано':
            return True
        else:
            self.logger.error(f"random_email Клиент не новый поле Гражданство заполнено, {text}")
            self.error_save_screenshot()
            raise AssertionError(f"random_email Клиент не новый поле Гражданство заполнено, {text}")

    def split_fio(self, text):
        text_list = text.split()
        surname = text_list[0]
        name = text_list[1]
        patronymic = text_list[2]
        return surname, name, patronymic
