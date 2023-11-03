from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardOtherDocuments(MainPage):

    PHOTOS_OTHER_DOCUMENTS = (By.XPATH, '//android.view.View[@content-desc="Шаблон документа"]')
    PHOTOS_PREVIEW = (By.XPATH, '//android.widget.ImageView[@content-desc="Фото документа привью"]')
    DOCUMENT_TYPS = ['Заявление заемщика (лицевая)', 'Заявление заемщика (оборотная)',
                     'Согласие на обработку персональных данных (лицевая)',
                     'Согласие на обработку персональных данных (оборотная)',
                     'Миграционная карта - лицевая сторона', 'Миграционная карта - оборотная сторона',
                     'Патент - лицевая сторона', 'Патент - оборотная сторона',
                     'Регистрация - лицевая сторона', 'Регистрация - оборотная сторона',
                     'Военный билет', 'Квитанция об оплате штрафов в ГИБДД',
                     'Чеки/квитанции об оплате патента', 'Полис ДМС/ОМС - лицевая сторона',
                     'Свидетельство о рождении', 'Справка УФМС', 'Трудовой договор первая страница',
                     'Трудовой договор вторая страница', 'Выписка по банковскому счету',
                     'Сертификат вакцинации от COVID-19', 'Печать о получении ВНЖ', 'Чеки оплаты займов в других МФО',
                     'Снимок мобильного приложения', 'Другое']

    BUTTON_ADD_PHOTOS_DOC = (By.XPATH, '//android.view.View[@content-desc="Кнопка Добавить фото"]')
    DOC_STATEMENT_BORROWER_FRONT_TEXT = 'Заявление заемщика (лицевая)'
    DOC_STATEMENT_BORROWER_OTHER_TEXT = 'Заявление заемщика (оборотная)'
    NAME_DOCUMENT = (By.XPATH, '//android.widget.TextView[@content-desc="Название документа"]')
    BACK_TO_DOCUMENTS = (By.XPATH, '//android.widget.ImageView[@content-desc="Возврат к списку"]')

    def scroll_preview_list_documents(self):
        """Открывает все привью документа записывает их в список name_preview"""
        name_preview = []
        flaf = True
        if self.field_presence_check(self.PHOTOS_PREVIEW):
            while flaf:
                self.logger.info(f"ШАГ ПРОКРУТКИ ПРИВЬЮ метод open_and_save_name_photos")
                elements_preview = self.search_all_elements(self.PHOTOS_PREVIEW)
                self.logger.info(f"КОЛИЧЕСТВО ЭЛЕМЕНТОВ elements_preview на странице  = {len(elements_preview)}")
                for step in range(len(elements_preview)):
                    self.select_element_by_number(self.PHOTOS_PREVIEW, step)
                    try:
                        text = self.check_text_by_selector(self.NAME_DOCUMENT)
                    except Exception:
                        self.logger.info(f"ЭЛЕМЕНТ ЕСТЬ, НАЖАТЬ НЕЛЬЗЯ, ИСПОЛЬЗУЕМ ПРОКРУТКУ")
                        self.scrolls_all(self.SCROLL_RIGHT_OTHER_DOC_PHOTO_DOCUMENTS)
                        self.select_element_by_number(self.PHOTOS_PREVIEW, step)
                        text = self.check_text_by_selector(self.NAME_DOCUMENT)

                    if not name_preview.count(text):
                        name_preview.append(text)
                    else:
                        if step == len(elements_preview) - 1:
                            self.logger.info(f"name_preview = {name_preview}")
                            self.logger.info(f"len(name_preview) = {len(name_preview)}")
                            return name_preview
                    self.driver.back()
                self.scrolls_all(self.SCROLL_RIGHT_OTHER_DOC_PHOTO_DOCUMENTS)

    def select_element_by_number(self, selector, nimber):
        """Находит все элементы селектора и нажимает на элемент с порядковым номером nimber"""
        try:
            new_elements_preview = self.search_all_elements(selector)
            element = new_elements_preview[nimber]
            element.click()
        except Exception as e:
            self.logger.error(f"select_element_by_number Возникла ошибка = {e}")
            self.error_save_screenshot()
            raise Exception(f"select_element_by_number = {e}")
