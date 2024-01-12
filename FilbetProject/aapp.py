import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

options = AppiumOptions().load_capabilities(
    {
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.example.filbet_stake",
        "appium:appActivity": ".MainActivity"
    }

)


print(options.capabilities)


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options, direct_connection=True)

el1 = driver.find_element(By.XPATH, "//android.view.View[@content-desc='I am 21 years old']")
el1.click()
el2 = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Login / Register']")
el2.click()
time.sleep(1)
el3 = driver.find_element(By.XPATH, "//android.view.View[@content-desc='I agree and understand the ']")
el3.click()
time.sleep(1)
el4 = driver.find_element(By.XPATH, "//android.view.View[@content-desc='I Agree']")

#滑动
driver.swipe(start_x=1018, start_y=433, end_x=1024, end_y=1488)
el4.click()
#拖拽
# driver.drag_and_drop(el1, el2)
# el5 = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Phone No.']")
# el5.send_keys('9696406798')

# 通过坐标输入文本（假设点击后弹出了一个输入框）
text = '9696406798'  # 替换为你要输入的文本内容
action = TouchAction(driver)
action.tap(x=395, y=657).perform()
action.wait(1000)  # 等待输入框弹出
# action.

#事件链TouchAction
#作用：构建相对比较复杂的，连续的触摸行为


print(driver.current_activity)

time.sleep(3)

# print(driver.current_package)
# print(driver.remove_app("com.example.filbet_stake"))
# print(driver.install_app("C:\\Users\\User1\\Downloads\\Filbet-Stake_release_[test]_1.0.20(21).apk"))

driver.quit()

