"""
    * **模块** 就好比是 **工具包**，要想使用这个工具包中的工具，就需要 **导入 import** 这个模块
    * 每一个以扩展名 `py` 结尾的 `Python` 源代码文件都是一个 **模块**
    * 在模块中定义的 **全局变量** 、 **函数** 都是模块能够提供给外界直接使用的工具
"""


def print_line(line, times):
    print(line * times)


def print_lines(line, times):
    i = 0
    while i < 5:
        print_line(line, times)
        i += 1


name = "熊志豪"
