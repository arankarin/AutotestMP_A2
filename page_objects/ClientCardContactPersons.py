from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardContactPersons(MainPage):

    # Контактные лица Селекторы
    CONTACT_PERSONS_BUTTON_NEW_CONTACT = (By.XPATH, '//android.view.View[@content-desc="Новый контакт"]/..')
    CONTACT_PERSONS_NEW_TYPE_CONNECTION = (By.XPATH, '//android.widget.TextView[@content-desc="Тип связи:"]')
    CONTACT_PERSONS_NEW_FIO = (By.XPATH, '//android.view.View[@content-desc="ФИО Контактное"]/..')
    CONTACT_PERSONS_PHONE_NUMBER = (By.XPATH, '//android.view.View[@content-desc="Номер телефона"]/..')

    # Вкладка Контактные лица заполение нового клиента
    NEW_TYPE_CONNECTION_BROTHER = (By.XPATH, '//android.widget.TextView[@content-desc="Брат"]')
    CONTACT_NEW_FIO_TEXT = 'Тест Первый'
    CONTACT_PHONE_NUMBER_TEXT = '79320000001'

    TYPE_CONNECTION_LIST = ['Не выбрано', 'Арендодатель', 'Бабушка', 'Брат', 'Брат жены (шурин)', 'Брат мужа (деверь)',
                       'Двоюродная сестра', 'Двоюродный брат', 'Дедушка', 'Должник', 'Дочь', 'Друзья',
                       'Дядя', 'Жена', 'Зять', 'Иное', 'Клиент', 'Коллега', 'Коллеги', 'Мама', 'Муж',
                       'Начальник', 'Невеста', 'Отец', 'Папа', 'Племянник(ца)', 'председатель махаллинского комитета',
                       'Прочее', 'Рабочий', 'Руководитель', 'Сват', 'Свекровь', 'Свёкр', 'Сестра',
                       'Сестра мужа (золовка)', 'Сноха', 'Соседи', 'Сын', 'Тесть', 'Тетя', 'Тёща']

    CONTACT_PERSONS_ALL = (By.XPATH, '//android.widget.TextView[@content-desc="ФИО"]')
    CONTACT_PERSONS_TYPE_CONNECTION_ALL = (By.XPATH, '//android.widget.TextView[@content-desc="Кем приходится"]')
    CONTACT_PERSONS_FIO_ALL = (By.XPATH, '//android.widget.TextView[@content-desc="Номер телефона"]')


    CONTACT_PERSONS_PHONE_NUMBER_IN_THE_LIST = (By.XPATH, '//android.widget.TextView[@content-desc="Номер телефона"]')

    TYPE_CONNECTION = 'Кем приходится'
    FIO = 'ФИО'
    PHONE_NUMBER = 'Номер телефона'

    def contact_person_details(self, selector, number, text_field, phone=False):
        """Сравниваем текст из text_field с текстом из поля с порядковым помером number,
         всех найденных элементов по селектору selector. Если поле содержит номер телефона необходимо передать
         phone=True"""
        all_elements = self.search_all_elements(selector)
        try:
            text_by_number_field = all_elements[number].text
            self.logger.info(f"contact_person_details text_by_number_field = {text_by_number_field}")
            if phone:
                text_by_number_field = self.editing_phone_number(text_by_number_field)
        except IndexError:
            self.logger.error(f"contact_person_details Нет элемента с порядковым номером = {number}")
            self.error_save_screenshot()
            raise IndexError(f"contact_person_details Нет элемента с порядковым номером = {number}")
        try:
            assert text_by_number_field == text_field
            self.logger.info(f"contact_person_details text_number = {text_by_number_field}")
        except AssertionError:
            self.logger.error(f"contact_person_details, элемнты не равны "
                              f"text_by_number = {text_by_number_field}, text_field = {text_field}")
            self.error_save_screenshot()
            raise AssertionError

    def text_field_contact_persons(self, value_list_contact_persons):
        """Получает value_list_contact_persons и возвращяет type_connection, fio, phone_number"""
        type_connection =value_list_contact_persons[0][0]
        fio = value_list_contact_persons[1][0]
        phone_number = value_list_contact_persons[2][0]
        self.logger.info(f"text_field_contact_persons type_connection = {type_connection}")
        self.logger.info(f"text_field_contact_persons fio = {fio}")
        self.logger.info(f"text_field_contact_persons phone_number = {phone_number}")

        return type_connection, fio, phone_number