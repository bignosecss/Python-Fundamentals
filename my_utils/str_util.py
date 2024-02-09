def str_reverse(s):
    """
    反转传入的字符串
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    if not isinstance(s, str):
        print("请传入一个字符串!")
    return s[::-1]


def substr(s, x, y):
    """
    按照给定的下标，完成给定字符串的切片操作
    :param s: 被切片的字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 切片完成的字符串
    """
    return s[x:y]


# 测试
if __name__ == '__main__':
    print(str_reverse("bignosecss"))
    print(substr("bignosecss", 2, -1))
