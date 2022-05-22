"""
    dir 内置函数
"""

"""
    在python中对象无所不在, 变量,数据,函数都是对象
    在python中可以使用下面两个方法来查看对象的属性和方法
        1. 在对象标识符/数据后输入".", 然后按下Tab键, ipython会提示该对象能够调用的方法列表
        2. 使用内置函数 dir 传入标识符/数据, 可以查看对象内的所有属性和方法
"""

"""
    | 序号 |   方法名   | 类型 | 作用                                         |
    | :--: | :--------: | :--: | -------------------------------------------- |
    |  01  | `__new__`  | 方法 | **创建对象**时，会被 **自动** 调用           |
    |  02  | `__init__` | 方法 | **对象被初始化**时，会被 **自动** 调用       |
    |  03  | `__del__`  | 方法 | **对象被从内存中销毁**前，会被 **自动** 调用 |
    |  04  | `__str__`  | 方法 | 返回**对象的描述信息**，`print` 函数输出使用 |
"""
