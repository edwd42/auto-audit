import os
import sys
import time

import openpyxl
import selenium
from openpyxl import load_workbook
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

# should print version 3.5 for pynput dependency
print("Python --version ==", sys.version)
print("openpyxl.__version__ ==", openpyxl.__version__)
print("selenium version ==", selenium.__version__)

url = 'https://www.RedCrossBlood.org/donate-blood/dlp/may-trauma-awareness-month'
driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')

os.chdir('/Users/melocal/MyDox/RedCross/Code4Good/WCAG2.0')
wb = openpyxl.load_workbook('RCB Top Sites B-3.xlsx')
sheetnames = wb.sheetnames
sheet0 = wb[sheetnames[0]]
print(sheet0.max_row)

# for i in range(2, sheet0.max_row):
for i in range(2, 5):
    # print(sheet0['A' + str(i)].value)
    url = 'https://' + sheet0['A' + str(i)].value
    driver.get(url)
    print(driver.title)
    time.sleep(0.1)
