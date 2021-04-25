import time
from plyer import notification
import requests
import json
import xlrd


def readExel(path):
    workBook = xlrd.open_workbook(path)
    sheet = workBook.sheet_by_index(0)
    print(sheet.cell_value(0, 0))



def reminder(data):
    pass


def wordAPI(url):
    pass


if __name__ == "__main__":
    readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")
