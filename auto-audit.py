import os

import openpyxl
from openpyxl import load_workbook

os.chdir('/Users/melocal/MyDox/RedCross/Code4Good/WCAG2.0')
wb = openpyxl.load_workbook('RCB Top Sites B-3.xlsx')
sheetnames = wb.sheetnames
sheet0 = wb[sheetnames[0]]
print(sheet0.max_row)

for i in range(2, sheet0.max_row):
    print(sheet0['A' + str(i)].value)
