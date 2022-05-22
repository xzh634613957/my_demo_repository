"""
    单例设计实例
"""
"""
    **单例** —— 让 **类** 创建的对象，在系统中 **只有** **唯一的一个实例**
        1. 定义一个 **类属性**，初始值是 `None`，用于记录 **单例对象的引用**
        2. 重写 `__new__` 方法
        3. 如果 **类属性** `is None`，调用父类方法分配空间，并在类属性中记录结果
        4. 返回 **类属性** 中记录的 **对象引用**
"""


# 这个类没有使用单例, 因此每次实例化的对象的地址都不一样, 说明对象不是同一个
class Class1(object):
    pass


class1 = Class1()
print(class1)
class2 = Class1()
print(class2)
# 可以看到返回的地址不同


# 下面这个类使用单例设计, 因此每次实例化的对象的地址都是同一个, 说明对象是同一个
class MusicPlayer(object):

    # 定义类属性, 记录第一次创建对象时__new__方法分配的内存地址
    instance = None

    # 重写__new__方法
    def __new__(cls, *args, **kwargs):

        # 1.判断 类属性instance 是否为空, 若为空, 说明还没有被赋值, 也就是说这个类还没有创建过对象
        if cls.instance is None:
            # 2.调用父类的__new__方法, 将父类__new__方法分配的内存地址赋值给第一次创建的对象的类属性instance
            cls.instance = super().__new__(cls)

        # 3.返回得到赋值的类属性
        return cls.instance


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
# 可以看到返回的地址是一样的
