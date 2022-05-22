"""
    递归: 函数调用自身的编程技巧称为递归
"""
"""
    递归函数的特点:
        * 函数内部的代码是相同的, 只是针对的参数不同, 处理的结果不同
        * 当参数满足一个条件时, 函数不再执行
            - 这个非常重要, 通常被称为递归的出口, 否则会出现死循环
"""


# 示例1
def demo1(num):
    print(num)
    # 递归的出口, 当参数满足某个条件时, 不再执行函数
    if num == 1:
        return

    # 自己调用自己
    demo1(num - 1)


demo1(3)


# 示例2
"""
    需求:
        * 定义一个函数 sum_numbers
        * 能够接收一个 num 的整数参数
        * 计算 1+2+...+num 的结果
"""


def sum_numbers(num):
    if num == 1:
        return 1
    temp = sum_numbers(num - 1)
    return num + temp


print(sum_numbers(3))
