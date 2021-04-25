import time
from plyer import notification
import requests
import json
import openpyxl


def readExel(path):
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)
    
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    
    # Loop will print all columns name
    for i in range(1, sheet_obj.max_row +1):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row = 1, column = i)
            print(cell_obj.value)


def reminder(data):
    pass


def wordAPI(url):
    pass


if __name__ == "__main__":
    readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")
