import logging
from selenium import webdriver
from pytest_xlsx.file import XlsxItem

driver = webdriver.Chrome()


def pytest_xlsx_run_step(item: XlsxItem):
    step = item.current_step
    print("step:", step)
    key = step["标记"]
    args = step["内容"]
    ass = step["断言"]
    driver.get(args)
    logging.warning(f"关键字={key},参数={args},断言={ass}")
