"""
当一个函数没有捕获并处理异常时，该异常会被传递到调用该函数的代码块。
如果调用函数的代码块也没有处理该异常，那么异常会继续向上传递，直到找到能够
处理该异常的代码块或程序中止运行。
"""


# 定义出现异常的方法
def func1():
    print("func1 开始执行")
    num = 1 / 0  # 除以 0 异常
    print("func1 结束执行")


# 定义一个无异常的方法，调用上面有异常的方法
def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")


# 定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常的信息是: {e}")

main()
