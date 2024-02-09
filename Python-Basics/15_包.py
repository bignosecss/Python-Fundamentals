# 导入自定义包中模块并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
#
# info_print1()


# 包中 __all__ 变量控制 import *
from my_package import *
my_module1.info_print1()
