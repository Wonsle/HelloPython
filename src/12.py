"""
Day 12: 進階函數與範圍 (Scope)**
  * 全域變數 (Global) vs 區域變數 (Local)。
  * 了解 `*args` (不定長度參數)。
"""

# 全域變數範例
x = 10  # 這是全域變數

def private_func():
    # 區域變數範例
    y = 5  # 這是區域變數
    print("Inside private_func, y =", y)

private_func()
print("Outside private_func, x =", x)