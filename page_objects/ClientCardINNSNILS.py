import allure
from selenium.webdriver.common.by import By
from page_objects.MainPages import MainPage

class ClientCardINNSNILS(MainPage):

    # ИНН/СНИЛС Селекторы
    HEADER_INN_SNILS = (By.XPATH, '//android.widget.TextView[@content-desc="ИНН/СНИЛС"]')
    HEADER_INN_SNILS_TEXT = 'ИНН/СНИЛС'
    INN_SNILS_CROSS = (By.XPATH, '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])')
    INN_CROSS = (By.XPATH, '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])[1]')
    SNILS_CROSS = (By.XPATH, '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])[2]')
    INN_TEXT_FIELD = (By.XPATH, '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])[1]/../..')
    SNILS_TEXT_FIELD = (By.XPATH, '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])[2]/../..')

    INN_CLIENT = '663207381000'
    SNILS_CLIENT = '09728187417'

    @allure.step
    def fill_field_inn_snils(self, selector, selector_cross, new_text):
        """Изменяет значение в поле ИНН или СНИЛС, принимает селектор поля, селектор крестика, текст ввода,
        возвращает value_list типа ['отсутствует', '(//android.view.View[@content-desc="ИНН и СНИЛС крестик"])[1]/../..']"""
        old_text = self.check_text_by_selector(selector)
        self.click_element(selector_cross)
        field = self.search_element(selector)
        if old_text == 'отсутствует':
            field.send_keys(new_text)
            value_list = [new_text, selector]
            return value_list
        else:
            self.click_element(selector_cross)
            value_list = ['отсутствует', selector]
            return value_list
