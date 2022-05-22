"""
    在使用单例设计时只执行一次初始化工作
"""
"""
    在每次使用 `类名()` 创建对象时，`Python` 的解释器都会自动调用两个方法：
        * `__new__` 分配空间
        * `__init__` 对象初始化
"""
"""
    * 在上一小节对 `__new__` 方法改造之后，每次都会得到 **第一次被创建对象的引用**
    * 但是：**初始化方法还会被再次调用**
"""
"""
    **需求**
        * 让 **初始化动作** 只被 **执行一次**
"""
"""
    **解决办法**
        1. 定义一个类属性 `init_flag` 标记是否 **执行过初始化动作**，初始值为 `False`
        2. 在 `__init__` 方法中，判断 `init_flag`，如果为 `False` 就执行初始化动作
        3. 然后将 `init_flag` 设置为 `True`
        4. 这样，再次 **自动** 调用 `__init__` 方法时，**初始化动作就不会被再次执行** 了
"""


class MusicPlayer(object):

    # 创建类属性, 记录对象的地址
    instance = None

    # 创建类属性, 记录是否执行过初始化操作
    init_flag = False

    # 重写父类的new方法
    def __new__(cls, *args, **kwargs):

        # 判断instance是否为空
        if cls.instance is None:
            # 调用父类的new方法赋值
            cls.instance = super().__new__(cls)

        # 返回instance记录的地址
        return cls.instance

    # 使初始化操作只执行一次
    def __init__(self):

        # 如果 init_flag 为真, 说明已经被初始化过了, 直接返回, 不再执行下面的初始化操作
        if MusicPlayer.init_flag:
            return

        # 执行初始化操作
        print("初始化音乐播放器")

        # 执行完初始化操作后修改 init_flag 为真
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()
# 可以看到, 有两个实例化对象, 但是只执行了一次初始化操作
