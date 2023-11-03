from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
# options.app = "/home/vis/Baibol/app-debug.apk"
options.app_package = "ru.baibol.manager2"
options.app_activity = ".ui.PrimaryActivity"
options.udid = "emulator-5554"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

# element = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.view.View")
# for i in element:
#
#     print(f"{i} текст: {i.text}")


# bt_1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[5]/android.view.View")
# bt_1.click()
# bt_1.click()
# bt_1.click()
# bt_1.click()
#
time.sleep(2)
#
#
# element_account = driver.find_element(by=AppiumBy.ID, value="android:id/text1")
# element_account.click()
# button_ok = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
# button_ok.click()

driver.close()

