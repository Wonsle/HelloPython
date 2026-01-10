"""
Day 9: 迴圈 (For Loops)
"""

for i in range(5):
    print(f"i:{i}")

print("=" *60)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"fruit:{fruit}")

print("=" *60)
print("帶索引的迴圈")
for index, fruit in enumerate(fruits):
    print(f"index:{index}, fruit:{fruit}")

print("=" *60)
print("點餐系統練習")
drinks = ["美式", "拿鐵", "奶茶"]
for drink in drinks:
    print(f"客官您的{drink}好了")

print("=" *60)
print("指定範圍與步進值")
for i in range(1,5,3):
    print(f"i:{i}")

print("=" *60)
print("倒數")
for i in range(5,0,-1):
    print(f"i:{i}")

print("=" *60)
print("倒數練習")
# 模擬 「奧運比賽倒數計時」，但是要有點變化。
# 任務：
# 從 30 秒開始倒數。
# 每次跳過 5 秒 (也就是 30, 25, 20...)。
# 最後數到 0 秒時停止 (要印出 0)。
# 最後印出一句 "比賽開始！"

for i in range(30, -1,-5):
    print(f"i:{i}")
    if(i==0):
        print("比賽開始！")