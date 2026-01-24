"""
19: OOP - 繼承與方法
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age


