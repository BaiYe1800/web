from webbrowser import Chrome

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from login import driver

print(1)
frame = driver.find_element(By.XPATH, 's')

driver.switch_to.frame(frame)
# *** 元素定位不到最大的可能就是因为： 在iframe种，需要切换到相应的frame
# 切换回主页面
driver.switch_to.default_content()
#主页面与frame的元素，不能互相操作

#下拉框操作、但是需要select标签的元素，否则无法使用。
sl1 = driver.find_element(By.XPATH, 's')
Select1 = Select(sl1)
Select1.select_by_value('4')

# 文件上传

#上传文件：先点击上传按钮、点击预览按钮、发送文件的绝对路径。


#每一个元素定位，都是一个元组，由两个字符串组成。

# @calssmethod
#   显式等待方法，封装在POM里面    WebDriverWait(driver,5).until(func) 好处，不需要等待固定时间，元素出现就继续执行。

#元素定位结合显示等待的使用。

#def find_element(self, by, value, driver, need_wait=False):

#封装BasePage

#夹具通常用于在测试之前进行一些准备工作（如创建数据库连接、初始化数据等），以及在测试之后进行清理操作（如关闭数据库连接、清理临时文件等）。
#夹具用于测试框架中的测试环境准备和清理，而装饰器用于修饰函数的行为。在测试框架中，通常可以使用装饰器来修饰夹具函数，以实现更灵活的夹具功能。
#   starts-with(@id, "xxxx")  可以在控制台  手写$x(//starts-with(@id, "xxxx")).textContent

#程序执行结果：P、S、F  通过、跳过、失败

@pytest.fixture
def driver():
    return Chrome()