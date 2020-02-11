# auto-audit

## Introduction:

auto-audit is a python script I wrote to automate the repetitive part of the Code4Good - WCAG 2.0 Accessibility Project where we pull a JIRA ticket and scan each of the 50 URLs in the spreadsheet attached to each ticket, and save the scan results to a .json file on GitHub.

## Scope:

this is a simple python script that has 3 functions:

- 1. read each line of the input spreadsheet
- 2. copy that url into the address bar of the browser
- 3. open the audit tool in the browser

## Tools and Technologies:

This script is written in Python 3.4
Imported modules include:
openpyxl for reading the spreadsheet,
selenium for opening the web page in the browser,
pyinput for sending keypress input to the browser

## Limitations:

I am first going to make this tool work in Safari. One of the limitations of working in Safari is that I am not experienced with Apple Script to programatically control the Safari browser Audit tool.

## Blockers

I am trying to run safaridriver under python 3.4 and get error KeyError: 'status' because safaridriver is not compatible with python 3.4
It works with python 3.5+ but then pynput requires python 3.4
So, I either do not use pynput or do not use safaridriver.
