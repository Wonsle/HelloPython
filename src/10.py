"""
Day 10: 迴圈 (While Loops) 與 控制
"""

number = 10

while number > 1:
    print(f"number:{number}")
    number-=1
    if number == 5 or number ==7:
        print(f"skip this number :{number}")
        continue
    if number == 2:
        break
