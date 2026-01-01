age = 30
print(f"Age: {age}")
print(type(age))
# name = "Alice"
name = 'Alice'
print("Name: {name}")
print(f"Name: {name=}")
print(type(name))
money= 1000.50
print(f"Money: ${money:.2f}")
print(type(money))

print(f"Name: {name}, Age: {age}, Money: ${money:.2f}")


header = "項目"
print(f"|{header:<10}|")  # 左對齊，寬度 10
print(f"|{header:>10}|")  # 右對齊，寬度 10
print(f"|{header:^10}|")  # 置中對齊，寬度 10

# 使用指定字元補齊空間
print(f"{header:=^20}")   # 輸出: =========項目=========