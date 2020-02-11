import os
import sys

import openpyxl
import selenium
from openpyxl import load_workbook
from selenium import webdriver

print(sys.version)  # should print version 3.4 for pynput dependency
print(openpyxl.__version__)

# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
# driver = webdriver.Safari()
# driver.get(
#     'https://www.RedCrossBlood.org/donate-blood/dlp/may-trauma-awareness-month')

os.chdir('/Users/melocal/MyDox/RedCross/Code4Good/WCAG2.0')
wb = openpyxl.load_workbook('RCB Top Sites B-3.xlsx')
sheetnames = wb.sheetnames
sheet0 = wb[sheetnames[0]]
print(sheet0.max_row)

# for i in range(2, sheet0.max_row):
for i in range(2, 5):
    print(sheet0['A' + str(i)].value)
# driver.get('https://' + sheet0['A' + str(i)].value)
# print(driver.title)
# time.sleep(0.1)
