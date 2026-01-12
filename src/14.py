"""
Day 14: 第二週總複習 & 實作
  小專案：猜數字遊戲 (電腦隨機產生數字，使用者輸入猜測，提示太大或太小)。
"""

import random

boom = random.randint(1, 100)
print("歡迎來到猜數字遊戲！請猜一個1到100之間的數字。")
while boom != input("請輸入1~100的數字: "):
    guess = int(input("請輸入1~100的數字: "))
    if guess < boom:
        print("太小了")
    elif guess > boom:
        print("太大了")
    else:
        print("恭喜你猜對了！")
        break