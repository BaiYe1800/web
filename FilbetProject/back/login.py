import logging
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pytest_xlsx.file import XlsxItem


driver = webdriver.Chrome()

url = 'https://admin.filbet-zi-test.com/'

driver.get(url)

driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/div[1]/div/div/input').send_keys(
    'RayTest')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(
    '123456')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/button').click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/a').screenshot('test.png')
print(driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[3]/div[9]/div[1]/span').text)
#获取所有cookie
# @allur
# allure generate report/ -o report/html
driver.get_cookies()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[12]/div/div/div/input').click()


# input("开启调试： ")
# driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li[12]').click()

#如果使用关键字驱动POM设计模式的用例设计特性：
    # 以页面为中心，页面越多越复杂。代码越多越复杂。
#关键字驱动KDT设计模式的用例设计特性：
    #以用户为中心，用户的操作能力是有限的

    #获取断言的逻辑，需要判断是否需要等待等。

#hook 是pytest非常核心的概念和机制，也是测试开发必须掌握的技能。
#当Excel用例呗执行时，会自动被调用。
def pytest_xlsx_run_step(item: XlsxItem):
    logging.warning(f"测试表格{item.current_step}")


driver.quit()
