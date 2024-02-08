"""
文件不存在，"w" "a" 模式会创建一个文件并写入内容。
文件存在，"w" 模式会把内容清空，然后写入内容。"a" 模式会在最后，追加写入文件。
"""
# 打开一个不存在的文件
f = open("test-write.txt", "w", encoding="UTF-8")

# write 写入
f.write("Hello World!")

# flush 刷新
# f.flush()

# 关闭文件
f.close()  # close() 方法内置了 flush 的功能
