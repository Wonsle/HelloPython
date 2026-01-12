"""
Day 13: 錯誤處理 (Try / Except)**
  * 捕捉異常：`ZeroDivisionError`, `ValueError`
"""

try:
    # print(10/0)
    throw_error = int("abc")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except:
    print("Other error occurred.")