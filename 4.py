"""
Day 4: 列表 (Lists)
"""

from pickle import TRUE


tablelist = ["Employee", "Organization", "Salary"]
print(tablelist)

tablelist.append("Location")
print(tablelist)

tablelist.remove("Employee")
print(tablelist)

tablelist.pop(0) # 移除索引為0的元素
print(tablelist)

tablelist.sort(reverse=True) # 排序列表
print(f"tablelist sort true: {tablelist}")
tablelist.sort(reverse=False) # 排序列表
print(f"tablelist sort false: {tablelist}")

extend_tablelist = ["Age", "Department"]
tablelist.extend(extend_tablelist) # 擴展列表
print(tablelist)

tablelist.insert(1, "Position") # 在索引1的位置插入元素
print(tablelist)

tablelist.remove("Position") # 移除值為"Position"的元素
print(tablelist)

tablelist.clear() # 清空列表
print(f"tablelist: {tablelist}")