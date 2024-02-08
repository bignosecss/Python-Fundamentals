# 基本捕获语法
try:
    f = open("E:/DevFile/StudyZone/hmit-python/abc.txt", "r", encoding="UTF-8")
except:
    print("出现了异常，因为文件不存在，我将 open 的模式更改为 w 模式去打开.")
    f = open("E:/DevFile/StudyZone/hmit-python/abc.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    # 1 / 0
    print(name)
except (NameError, ZeroDivisionError) as n:
    print("出现了变量未定义 或者 除以 0 的异常")
    print(n)

# 捕获所有异常，基本语法同样捕获所有异常
try:
    f = open("E:/DevFile/StudyZone/hmit-python/abc.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现了异常")
else:
    print("耶斯，没有异常！")
finally:
    print("我是 finally")
    f.close()
