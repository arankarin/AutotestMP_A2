import os
import logging
import datetime

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from page_objects.MainPages import MainPage
from appium.webdriver.common.appiumby import AppiumBy
import time


def pytest_addoption(parser):
    parser.addoption("--appium_server", action="store", default="http://127.0.0.1:4723/wd/hub")
    parser.addoption("--package", action="store", default="ru.baibol.manager2")
    parser.addoption("--activity", action="store", default="presentation.PrimaryActivity")
    parser.addoption("--udid", action="store", default="emulator-5554")
    parser.addoption("--log_level", action="store", default="DEBUG")



@pytest.fixture
def mp(request):
    appium_server = request.config.getoption("--appium_server")
    options = UiAutomator2Options()
    options.app_package = request.config.getoption("--package")
    options.app_activity = request.config.getoption("--activity")
    options.udid = request.config.getoption("--udid")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    name = request.node.name[0:43]
    file_handler = logging.FileHandler(f"logs/{name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===>START Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    driver = webdriver.Remote(appium_server, options=options)

    driver.log_level = log_level
    driver.logger = logger

    yield driver

    logger.info("===>FINISH Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    driver.quit()


@pytest.fixture(params=['123f@fdg.ru', 'sdfsdf@123.ru', '123@123.ru', '123@123.ss'])
def params_positive_mail(request):
    return request.param

@pytest.fixture(params=['123f', 'sdfsdf@', '123@.ru', '123@ss', '123@ghg.'])
def params_negative_mail(request):
    return request.param

@pytest.fixture(params=['1', 'q', 'qwe', 'qwe asd', 'абвг', 'абвг деёжз'])
def params_positive_old_loan(request):
    return request.param

@pytest.fixture()
def enable_notifications(mp):
    page_mp = MainPage(mp)
    page_mp.click_element(page_mp.BUTTON_CLEAR)
    page_mp.click_element(page_mp.SWITH_NOTIFICATIONS)
    page_mp.click_element(page_mp.JUMP_UP)
