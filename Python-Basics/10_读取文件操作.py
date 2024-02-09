# 打开文件
import time

# f = open("../test-text.txt", "r", encoding="UTF-8")
# print(type(f))

# 读取文件 - read()
# print(f"读取 10 个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果是：{f.read()}")

# 读取文件的全部行，封装到列表中 - readLines()
# lines = f.readlines()
# print(f"lines 对象的类型：{type(lines)}")
# print(f"lines 对象的内容：{lines}")

# 读取文件 - readLine()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for 循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# 文件关闭
# f.close()

# with open 语法操作文件,可以自动关闭
with open("../test-text.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
