import time
from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardVisitInspeckion(MainPage):
    VISIT_INSPECTION_BUTTON_CREATE = (By.XPATH, '//android.view.View[@content-desc="Кнопка Создать визит-осмотр"]')
    VISIT_INSPECTION_ADDRESS = (By.XPATH, '//android.widget.TextView[@content-desc="Визит-осмотры Адрес"]')
    VISIT_INSPECTION_PHONE = (By.XPATH, '//android.widget.TextView[@content-desc="Визит-осмотры Номер телефона"]')
    VISIT_INSPECTION_COMMENT = (By.XPATH, '//android.view.View[@content-desc="Комментарий визит-осмотры"]/..')
    VISIT_INSPECTION_ALL_PHOTOS_WORK = (By.XPATH, '(//android.view.View[@content-desc="ВизитОсмотрРабота"]/..)')
    VISIT_INSPECTION_ALL_PHOTOS_HOME = (By.XPATH, '(//android.view.View[@content-desc="ВизитОсмотрДом"]/..)')
    VISIT_INSPECTION_GEOPOZITION = (By.XPATH, '//android.view.View[@content-desc="Геопозиция"]')
    VISIT_INSPECTION_GEOPOZITION_TEXT_IN_PHOTO = (By.XPATH, '//android.widget.TextView[@content-desc="Геопозиция"]')
    VISIT_INSPECTION_SAVE = (By.XPATH, '//android.view.View[@content-desc="Сохранить визит-осмотры"]')

    VISIT_INSPECTION_PHOTO_GEOPOZITION = (By.XPATH, '//android.widget.ImageView[@content-desc="Фото Геопозиция Визит-осмотр"]')


    def check_address_vivit_inspection(self, address_home, address_job, place_of_inspection):
        if address_home == address_job:
            place_of_inspection = 'Работа'
        if place_of_inspection == 'Дом':
            selector = self.get_selector_by_text(address_home)
            text_address = address_home
        else:
            selector = self.get_selector_by_text(address_job)
            text_address = address_job
        return selector, text_address

    def check_phone_vivit_inspection(self, phone, phone_main, phone_second):
        self.logger.info(f"check_phone_vivit_inspection phone = {phone}")
        self.logger.info(f"check_phone_vivit_inspection phone_main = {phone_main}")
        self.logger.info(f"check_phone_vivit_inspection phone_second = {phone_second}")
        new_phone_main = phone_main.replace('-', ' ')
        new_phone_second = phone_second.replace('-', ' ')
        if phone == 'Дополнительный' and phone_second != '':
            self.click_element(self.VISIT_INSPECTION_PHONE)
            selector = self.get_selector_by_text(new_phone_second)
            self.click_element(selector)
            text_phone = new_phone_second
        else:
            text_phone = new_phone_main

        return text_phone

    def name_photo_vivit_inspection(self, place_of_inspection):
        if place_of_inspection == 'Дом':
            self.field_presence_check(self.VISIT_INSPECTION_ALL_PHOTOS_HOME, wait_time=0.5)
        else:
            self.field_presence_check(self.VISIT_INSPECTION_ALL_PHOTOS_WORK, wait_time=0.5)

    def select_photos_vivit_inspection(self,place_of_inspection):
        if place_of_inspection == 'Дом':
            elements = self.search_all_elements(self.VISIT_INSPECTION_ALL_PHOTOS_HOME)
        else:
            elements = self.search_all_elements(self.VISIT_INSPECTION_ALL_PHOTOS_WORK)
        return elements

    def add_photo_visit_inspection(self, place_of_inspection):
        for step in range(4):
            elements = self.select_photos_vivit_inspection(place_of_inspection)
            element = elements[0]
            time.sleep(1)
            element.click()
            if self.field_presence_check(self.CAMERA_PERMISSION_BUTTON, wait_time=0.5):
                self.click_element(self.CAMERA_PERMISSION_BUTTON)
            self.name_photo_vivit_inspection(place_of_inspection)
            self.click_element(self.MAKE_PHOTO)
