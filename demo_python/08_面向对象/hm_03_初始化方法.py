"""
    初始化方法
"""
"""
    当使用类名创建对象时, 会自动执行以下操作:
        1. 为对象在内存中分配空间---创建对象
        2. 为对象的属性设置初始值---初始化方法(__init__)(类似于构造函数)
    这个初始化方法就是 __init__ 方法, __init__ 是对象的内置方法, 可以直接调用
"""
"""
    在开发中, 如果希望在创建对象的同时就设置对象的属性, 可以对__init__方法进行改造
        1. 把希望设置的属性值, 定义为__init__方法的形参
        2. 在方法内部使用 self.属性 = 形参 来接收外部传递的参数
        3. 在创建对象时, 使用 类名(属性1, 属性2,...) 调用对象属性
"""


# case1 初始化方法
class Cat:
    def __init__(self):
        print("初始化函数的调用")
        self.name = "Tom"  # 在初始化方法内部定义属性


tom = Cat()  # 程序会自动调用类的初始化方法
print(tom.name)  # 在初始化方法内部定义属性


# case2 利用参数设置属性的初始值
class Dog:
    def __init__(self, new_name):
        print("初始化方法的调用")
        self.name = new_name

    def eat(self):
        print("%s在啃骨头" % self.name)


dog = Dog("小白")
dog.eat()
