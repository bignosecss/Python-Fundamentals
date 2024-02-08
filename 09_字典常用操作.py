dict1 = {"name": "Bard", "age": 1}

# 访问值
print(dict1["name"])  # 输出: Bard

# 添加元素
dict1["language"] = "Python"
print(dict1)  # 输出: {'name': 'Bard', 'age': 1, 'language': 'Python'}

# 使用 update() 方法添加元素
dict1.update({"city": "New York"})
print(dict1)  # 输出: {'name': 'Bard', 'age': 1, 'language': 'Python', 'city': 'New York'}

# 删除元素
del dict1["age"]
print(dict1)  # 输出: {'name': 'Bard', 'language': 'Python'}

# 使用 pop() 方法删除元素
dict1.pop("language")
print(dict1)  # 输出: {'name': 'Bard'}

dict1 = {"name": "Bard", "age": 1, "language": "Python"}

# 检查键是否存在
print("name" in dict1)  # 输出: True

# 遍历字典
dict1 = {"name": "Bard", "age": 1, "language": "Python"}
for key, value in dict1.items():
    print(f"{key}: {value}")

# 输出:
# name: Bard
# age: 1
# language: Python
