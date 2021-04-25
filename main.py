import datetime
from plyer import notification
import requests
import json
import openpyxl


def readExel(path):
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)
    
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    
    records = list()

    # Loop will print all columns name
    for j in range(1, sheet_obj.max_row +1):
        for i in range(1, max_col + 1):
            # row_obj = sheet_obj.cell(row =j , column = i)
            a = sheet_obj.cell(row=j, column=i)
            print(a.value)
            records.append(a.value)
    records = [[records[i], records[i+1]] for i in range(0, len(records), 2)]
    return records
    


def reminder(data):
    notification.notify(
        
    )
    pass


def wordAPI(url):
    pass


if __name__ == "__main__":
    readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")
