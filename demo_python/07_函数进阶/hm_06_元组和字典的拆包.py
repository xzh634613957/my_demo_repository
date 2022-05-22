"""
    当需要将一个元组变量和一个字典变量传递给函数时需要用到拆包
"""
"""
    * 在调用带有多值参数的函数时, 如果希望:
        - 将一个元组变量直接传递给args
        - 将一个字典变量直接传递给kwargs
    * 此时就需要使用拆包,简化参数的传递
    * 拆包的方式:
        - 在元组变量前增加一个 *
        - 在字典变量前增加两个 *
"""


# 当不使用拆包时
def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

demo(gl_nums, gl_dict)  # 如果不使用拆包, 程序会将元组变量和字典变量视为一个元组变量
demo(*gl_nums, **gl_dict)
