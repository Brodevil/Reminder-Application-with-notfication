import datetime
from plyer import notification
import requests
import json
import openpyxl


def readExel(path):
    """Read the Exel fiel using openpyxl and return the 2d list as 1st will the time and 2nd will the pourpose """
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)
    
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    
    records = list()

    # Loop will print all columns name
    for j in range(1, sheet_obj.max_row +1):
        for i in range(1, max_col + 1):
            a = sheet_obj.cell(row=j, column=i)
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
    # Giving the excel file's path as a parameters
    exel = readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")  
    print(exel)