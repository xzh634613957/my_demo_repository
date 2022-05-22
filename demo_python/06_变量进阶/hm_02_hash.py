"""
    * `Python` 中内置有一个名字叫做 `hash(o)` 的函数
      * 接收一个 **不可变类型** 的数据作为 **参数**
      * **返回** 结果是一个 **整数**
    * `哈希` 是一种 **算法**，其作用就是提取数据的 **特征码（指纹）**
      * **相同的内容** 得到 **相同的结果**
      * **不同的内容** 得到 **不同的结果**
    * 在 `Python` 中，设置字典的 **键值对** 时，会首先对 `key` 进行 `hash` 已决定如何在内存中保存字典的数据，以方便 **后续** 对字典的操作：**增、删、改、查**
      * 键值对的 `key` 必须是不可变类型数据 (字符串, 数字, 元组)
      * 键值对的 `value` 可以是任意类型的数据
"""

print(hash(1))
print(hash(1))
print(hash("hello"))
print(hash("hello1"))
print(hash("hello1"))
print(hash((1, 2)))

num1 = 10
num2 = 20


def add_int1():
    temp = num1
    num1 = num2
    num2 = temp
    print(num1)
    return num1, num2


add_int1()


