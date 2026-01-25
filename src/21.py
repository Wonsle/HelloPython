"""
Day 21: 第三週總複習 & 實作**
   📝 **小專案：簡易記帳程式** (使用 Class 管理帳目，並將資料儲存於 CSV 檔案)。
"""

from asyncio import streams
import csv
from datetime import datetime
import decimal
from encodings import utf_8
import os

class Payment:
    buy_time: datetime
    description:str
    money: float

    def buy(self, buy_time, description, money) -> None:
        self.buy_time = buy_time
        self.description = description
        self.money = money

        filename = 'buy_detail.csv'

        # 檢查檔案是否存在，這決定了我們是否需要寫 Header
        # C#: File.Exists(path)
        file_exists = os.path.isfile(filename)
        f=None
        f = open(filename,'a',encoding='utf-8')
        fieldnames = ['date', 'description', 'money']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'date': self.buy_time,
            'description': self.description,
            'money': self.money
        })

        f.close()

while True:
    pment = Payment
    pment().buy(
        input("日期"),
        input("描述"),
        input("金額")
    )

