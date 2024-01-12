import time

import allure
import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = 'https://admin.filbet-zi-test.com/'
driver.get(url)


@pytest.mark.parametrize("username,password", [["RayTest", "123456"]])
@allure.step("我是测试步骤001")
def test_admin(password, username):
    driver.maximize_window()

    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/div[1]/div/div/input').send_keys(
        username)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(
        password)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/form/button').click()

    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/a').screenshot('test.png')
    allure.attach()
    print(driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[3]/div[9]/div[1]/span').text)


