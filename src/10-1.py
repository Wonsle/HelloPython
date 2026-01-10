"""
Day 10: 迴圈 (While Loops) 與 控制 擴充
使用 while 迴圈、break 與 continue 敘述來控制程式碼執行流程。
本範例展示了一個簡單的猜數字遊戲（終極密碼）。
"""

# 終極密碼

import random

boom = random.randint(1, 20)

while True:
    guess = int(input("Please guess a number between 1 and 20: "))
    if guess == boom:
        print('boom!')
        break
    continue