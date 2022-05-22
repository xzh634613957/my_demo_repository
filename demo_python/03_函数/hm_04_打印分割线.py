"""
* 定义一个函数能够打印 5 行 的分隔线，分隔线要求符合 需求 3
> 提示：工作中针对需求的变化，应该冷静思考，**不要轻易修改之前已经完成的，能够正常执行的函数**！
**需求 3**
* 定义一个函数能够打印 **任意重复次数** 的分隔线
"""


def print_line(line, times):
    print(line * times)


def print_lines(line, times):
    i = 0
    while i < 5:
        print_line(line, times)
        i += 1


print_lines("-", 20)
