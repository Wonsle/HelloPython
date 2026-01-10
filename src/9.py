"""
Day 9: 迴圈 (For Loops)
"""

for i in range(5):
    print(f"i:{i}")


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"fruit:{fruit}")

for index, fruit in enumerate(fruits):
    print(f"index:{index}, fruit:{fruit}")

drinks = ["美式", "拿鐵", "奶茶"]
for drink in drinks:
    print(f"客官您的{drink}好了")