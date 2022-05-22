"""
    定义支持多值参数的函数
"""
"""
    * 有时可能需要一个函数能够处理的参数个数是不确定的,这个时候就可以使用多值参数
    * Python 中有两种多值参数
        1. 参数名前增加一个"*"可以接收元组
        2. 参数名前增加两个"*"可以接收字典
    * 一般在给多值参数命名时,习惯使用以下两个名字:
        1. *args --- 存放元组参数, 前面有一个 *
        2. **kwargs --- 存放字典参数, 前面有两个 * 
    * args 是 arguments 的缩写, 有变量的含义
    * kw 是 keyword 的缩写, kwargs 可以记忆键值对参数
"""


# case
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
