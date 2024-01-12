from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction

options = AppiumOptions().load_capabilities(
    {
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.example.filbet_stake",
        "appium:appActivity": ".MainActivity"
    }

)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options, direct_connection=True)


action = TouchAction(driver)



