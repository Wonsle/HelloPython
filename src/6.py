"""
Day 6: 元組 (Tuples) 與 集合 (Sets)
"""

# 元組 (Tuples)
print(f"{'tuple':=^60}")
# 建立元組
my_tuple = (1, 2, 3, 4, 5)
print(f"My tuple: {my_tuple}")

# 訪問元組元素
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")

# 元組不可變更
# my_tuple[0] = 10  # 這行會報錯

# Sets (集合)
print(f"{'set':=^60}")
# 建立集合
my_set = {1, 2, 2,3,3, 3, 4,4,4, 5,5,6}
print(f"My set: {my_set}")

setA = {1, 2, 3}
setB = {3, 4, 5}
print(f"Union: {setA | setB}")
print(f"Intersection: {setA & setB}")
print(f"Difference: {setA - setB}")