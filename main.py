import datetime
from plyer import notification
import requests
import json
import openpyxl


def readExel(path):
    """Read the Exel file using openpyxl and return the 2d list as 1st will the time and 2nd will the purpose """
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)

    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column

    records = list()

    # Loop will print all columns name
    for j in range(1, sheet_obj.max_row + 1):
        for i in range(1, max_col + 1):
            a = sheet_obj.cell(row=j, column=i)
            records.append(a.value)
    records = [[records[i], records[i + 1]] for i in range(0, len(records), 2)]
    return records


def reminder(data):
    notification.notify(
        title="Attempt 20-20-20 Eyes Exercise",
        message="After every 20 minutes to give rest to your eyes see 20 meter long from your original distance in nature for 20 sec. Which defenatly safe the your eyes",
        app_icon=r"E:\ADMIN\Pictures\Saved Pictures\abhinav.ico",
        timeout=12
    )


def API(url):
    pass


if __name__ == "__main__":
    # Giving the excel file's path as a parameters
    exel = readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")
    print(exel)
