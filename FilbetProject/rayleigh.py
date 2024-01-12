import openpyxl
from pytest_xlsx.file import XlsxItem
import logging

workbook = openpyxl.load_workbook(r'C:\Users\User1\Desktop\test111.xlsx')

sheet = workbook.active

for row in sheet.iter_rows(values_only=True):
    print(row)

A1 = sheet['A1']
print(A1.value)

# logging.warning(f"测试表格{item.current_step}")
