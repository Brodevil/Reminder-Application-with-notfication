import time
from plyer import notification
import requests
import json
import pandas as pd



def readExel(path):
    # xl_file = pd.ExcelFile(path)

    df = pd.read_excel("Remind_data.xlsx", index_col=0)     
    print(df.head()) # print the first 5 rows

    # print(dfs)



def reminder(data):
    pass


def wordAPI(url):
    pass


if __name__ == "__main__":
    readExel("M:\ADMIN\Critical Data\VS-Code\Reminder Application with Notification\Remind_data.xlsx")
