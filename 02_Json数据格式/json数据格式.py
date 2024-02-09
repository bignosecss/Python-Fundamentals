"""
JSON 是一种轻量级的数据交换格式，采用完全独立于编程语言的文本格式来存储和表示数据（就是字符串）
Python 语言使用 JSON 有很大优势:
JSON 无非就是一个单独的字典或一个内部元素都是字典的列表
所以 JSON 可以直接和 Python 的字典或列表进行无缝转换
"""


import json
# 准备列表，列表内每一个元素都是字典，将其转换为 JSON
data = [{"name": "小红", "age": 12}, {"name": "大棒", "age": 21}, {"name": "小黄", "age": 16}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为 JSON
d = {"name": "小慧", "age": "21", "addr": "xt"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将 JSON 字符串转换为 Python 数据类型 [{K: v, k: v}, {k: v, k:v}]
s = '[{"name": "小红", "age": 12}, {"name": "大棒", "age": 21}, {"name": "小黄", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)

# 将 JSON 字符串转换为 Python 数据类型 {k: v, k: v}
s = '{"name": "小慧", "age": "21", "addr": "xt"}'
d = json.loads(s)
print(type(d))
print(d)
