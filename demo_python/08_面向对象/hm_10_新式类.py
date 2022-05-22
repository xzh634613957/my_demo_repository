"""
    新式类和旧式类
"""
"""
    object 是 Python 为所有对象提供的基类, 提供了一些内置的属性和方法, 可以使用 dir() 函数查看
"""
"""
    * 新式类: 以 object 为基类的类. 推荐使用
    * 经典类: 不以 object 为基类的类, 不推荐使用
"""
"""
    * 在 `Python 3.x` 中定义类时，如果没有指定父类，会 **默认使用** `object` 作为该类的 **基类** —— `Python 3.x` 中定义的类都是 **新式类**
    * 在 `Python 2.x` 中定义类时，如果没有指定父类，则不会以 `object` 作为 **基类**
"""
"""
    重要:
        为了保证编写的代码能够同时在 `Python 2.x` 和 `Python 3.x` 运行！
        今后在定义类时，**如果没有父类，建议统一继承自 `object`** 
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


Person("小明", 20)
