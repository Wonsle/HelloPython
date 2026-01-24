"""
Day 18: 物件導向 (OOP) - 類別與物件
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age

# 建立 Dog 類別的物件
dog = Dog("Abby",8)
print(dog.bark())
print(dog.get_age())