"""
Day 5: 字典 (Dictionaries)
"""

employee = {
    "name": "John Doe",
    "age": 30,
    "jobtitle": "Software Engineer",
    "skills": ["Python", "JavaScript", "SQL"]}

print(f"{employee["name"]}")
print(f"{employee["age"]}")
print(f"{employee["jobtitle"]}")
print(f"{employee["skills"]}")

print(f"{'新增與修改字典資料':=^60}")
employee.update({"age": 25})
print(f"{employee["age"]}")
employee["department"] = "Development"
print(f"{employee["department"]}")
employee.pop("department")
# print(f"{employee["department"]}") # 不安全取值，會報錯
print(f"{employee.get("department","沒有department")}")  # 安全取值，不會報錯，會回傳 None

print(f"{'遍歷字典':=^60}")
for key, value in employee.items():
    print(f"{key}: {value}")

print(f"Employee keys: {employee.keys()}")
print(f"Employee values: {employee.values()}")
