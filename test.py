# ============================================
# 常用 Python 語法範例
# ============================================

# 1. 變數與資料型別
name = "Python"
age = 30
price = 19.99
is_active = True

# 2. 列表 (List)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
# 3. 字典 (Dictionary)
person = {"name": "John", "age": 25, "city": "Taipei"}

# 4. for 迴圈
for fruit in fruits:
    print(fruit)

# 5. while 迴圈
count = 0
while count < 3:
    print(count)
    count += 1

# 6. 條件判斷
x = 10
if x > 5:
    print("x 大於 5")
elif x == 5:
    print("x 等於 5")
else:
    print("x 小於 5")

# 7. 函式定義
def greet(name):
    """這是一個問候函式"""
    return f"Hello, {name}!"

# 8. 類別定義
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# 9. 例外處理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("無法除以零")
finally:
    print("執行完畢")

# 10. 列表推導式
squares = [x ** 2 for x in range(10)]

# 11. Lambda 函式
add = lambda a, b: a + b

# 12. 檔案操作
# with open("file.txt", "r") as f:
#     content = f.read()