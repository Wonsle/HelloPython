"""
Day 3: 數學運算與字串處理
"""
print(f"{'float float':=^60}")

# 基本數學運算
a=10
b=2.5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

print(f"{'string':=^60}")

# 字串處理方法
name = "allen lee"
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.replace("Lee", "Wang"))
print(name.split(" "))
print(len(name))

# 字串連接
print(f"{'join':=^60}")
fruits = ["apple", "banana", "cherry"]
print("|".join(fruits))

print(f"{'strip':=^60}")
# 去除空白

text = "   Hello, World!   "
print(text.strip())
print(text.rstrip())
print(text.lstrip())

# 字串替換
print(f"{'replace':=^60}")

print(text.strip().replace("Hello", "Hi"))
# 字串搜尋與檢查

print(f"{'search':=^60}")
text = "Hello, welcome to the world of Python programming."
print(text.find("welcomes"))
print(name.find("Hello"))
print(text.startswith("Hello"))
print(text.startswith("Hellox"))
print(text.endswith("programming."))
print(text.endswith("programming"))
print(text.count("e"))

# 數值檢查
print(f"{'check':=^60}")

number = "12345"
print(number.isdigit()) # 是否全為數字
print(number.isalpha()) # 是否全為字母
print(number.isalnum()) # 是否為字母或數字
print(name.islower())  # 是否全為小寫
print(name.isupper())  # 是否全為大寫
print(name.istitle())  # 是否為標題格式

