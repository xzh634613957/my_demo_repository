"""
    > 定义函数时，**是否接收参数，或者是否返回结果**，是根据 **实际的功能需求** 来决定的！

    1. 如果函数 **内部处理的数据不确定**，就可以将外界的数据以参数传递到函数内部
    2. 如果希望一个函数 **执行完成后，向外界汇报执行结果**，就可以增加函数的返回值
"""

"""
    1. 用元组的方式返回多个返回值
"""


def measure():
    temp = 39
    wetness = 50
    # 元组可以包含多个数据, 因此可以使用元组来让函数一次返回多个值
    # 这里元组的小括号可以省略
    return temp, wetness


result = measure()
print(result)

# 如果希望单独处理返回的元组中的元素, 可以使用多个变量, 并一次接受函数的返回结果
# 此时变量的个数应该与元组中的个数保持一致
gl_temp, gl_wetness = measure()
print(type(print(gl_temp, gl_wetness)))
