"""
Day 16: 檔案讀寫 (File I/O)**
  * `open()`, `read()`, `write()`。
  * 上下文管理器：`with open('data.txt', 'w') as f:`。
"""

# import fs

# f = open('data.txt', 'w')
# f.write('Hello, World!\n')
# f.write('This is a test file.\n')
# f.close()

f = open('data.txt', 'r')
content = f.read()
print(content)
f.close()