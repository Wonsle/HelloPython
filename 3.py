"""
Day 3: 數學運算與字串處理
"""
print(f"{'float float':=^60}")


a=10
b=2.5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

print(f"{'string':=^60}")

name = "allen lee"
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.replace("Lee", "Wang"))
print(name.split(" "))
print(len(name))

print(f"{'join':=^60}")
fruits = ["apple", "banana", "cherry"]
print("|".join(fruits))

print(f"{'strip':=^60}")

text = "   Hello, World!   "
print(text.strip())
print(text.rstrip())
print(text.lstrip())

print(f"{'replace':=^60}")

print(text.strip().replace("Hello", "Hi"))

print(f"{'search':=^60}")
text = "Hello, welcome to the world of Python programming."
print(text.find("welcomes"))
print(name.find("Hello"))
print(text.startswith("Hello"))
print(text.startswith("Hellox"))
print(text.endswith("programming."))
print(text.endswith("programming"))
print(text.count("e"))
