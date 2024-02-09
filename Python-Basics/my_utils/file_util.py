def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台
    :param file_name: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f"文件中全部的内容:\n {f.read()}")
    except Exception as e:
        print(f"文件不存在: {e}")
    else:
        print(f"正常读取文件 '{file_name}'")
    finally:
        if f:
            print("关闭文件")
            f.close()


def append_to_file(file_name, data):
    """
    将给定数据添加到目标文件中
    :param file_name: 目标文件
    :param data: 被添加的数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.close()


if __name__ == '__main__':
    print_file_info("../../bill.txt")
    # append_to_file("../test-write.txt", " hello ")
