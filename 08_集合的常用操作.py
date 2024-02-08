# 集合的定义：
# 用于存储和组织数据的无序且不重复的元素集合

# 创建集合
set_1 = set()
set_2 = {1, 2, 3, "a", "b", "c"}

# 常用操作
# 添加元素：使用 add() 方法添加元素到集合中
set1 = {1, 2, 3}
set1.add(4)
print(set1)  # output: {1, 2, 3, 4}

# 删除元素：使用 remove() 方法删除元素
set1.remove(2)
print(set1)  # output: {1, 3, 4}

# 检查元素是否存在：使用 in 运算符检查匀速是否存在于集合中
print(2 in set1)  # output: False

# 集合运算
# 并集：使用 | 运算符或 union() 方法计算两个集合的并集
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1 | set2
print(set3)  # output: {1, 2, 3, 4}

# 交集：使用 & 运算符或 intersection() 方法计算两个集合的交集
set3 = set1 & set2
print(set3)  # output: {2, 3}

# 差集：使用 - 运算符或 difference() 方法计算两个集合的差集
set3 = set1 - set2
print(set3)  # output: {1}
