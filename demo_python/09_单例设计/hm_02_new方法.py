"""
    new 方法
"""
"""
    使用 **类名()** 创建对象时，`Python` 的解释器 **首先** 会 调用 `__new__` 方法为对象 **分配空间**
    然后再将 对象的引用 传给对象的初始化方法(self)
"""
"""
    * `__new__` 是一个 由 `object` 基类提供的 **内置的静态方法**，主要作用有两个：
          * 1) 在内存中为对象 **分配空间**
          * 2) **返回** 对象的引用
    * `Python` 的解释器获得对象的 **引用** 后，将引用作为 **第一个参数**，传递给 `__init__` 方法
"""
"""
    * 重写 `__new__` 方法 **一定要** `return super().__new__(cls)` 
    * 否则 Python 的解释器 **得不到** 分配了空间的 **对象引用**，**就不会调用对象的初始化方法**
    * 注意：`__new__` 是一个静态方法，在调用时需要 **主动传递** `cls` 参数
"""


class MusicPlayer(object):

    # 重写父类(object)中的__new__方法
    def __new__(cls, *args, **kwargs):
        # 1.在创建对象时, new方法会被自动调用(就跟__init__一样)
        print("new函数的作用: 分配空间, 返回引用")

        # 2.为创建的对象分配内存空间
        instance = super().__new__(cls)  # 调用父类的方法得到分配的空间
        # 注意__new__是静态方法, 需要传入cls(特殊要求?)

        # 3.返回对象的引用
        return instance

    # 定义初始化方法
    def __init__(self):
        print("初始化音乐播放器对象")


# 实例化对象
player = MusicPlayer()
print(player)
