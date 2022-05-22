"""
    设计一个 Game 类
"""
"""
    属性： 
        * 定义一个 **类属性** `top_score` 记录游戏的 **历史最高分**
        * 定义一个 **实例属性** `player_name` 记录 **当前游戏的玩家姓名**
"""
"""
    方法：
        * **静态方法** `show_help` 显示游戏帮助信息
        * **类方法** `show_top_score` 显示历史最高分
        * **实例方法** `start_game` 开始当前玩家的游戏
"""
"""
    主程序步骤
        * 1) 查看帮助信息
        * 2) 查看历史最高分
        * 3) 创建游戏对象，开始游戏
"""
"""
    案例小结:
        1. **实例方法** —— 方法内部需要访问 **实例属性**
             * **实例方法** 内部可以使用 **类名.** 访问类属性
        2. **类方法** —— 方法内部 **只** 需要访问 **类属性**
        3. **静态方法** —— 方法内部，不需要访问 **实例属性** 和 **类属性**
"""
"""
    实例方法 --- 可以访问实例属性和类属性
    类方法 ---  可以访问类属性
    静态方法 --- 都不可以访问
"""


class Game(object):

    # 定义类属性
    top_score = 0

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print("当前的历史最高分是: %d分" % cls.top_score)

    # 定义静态方法
    @staticmethod
    def show_help():
        print("帮助信息: 加油哦~")

    # 定义初始化方法
    def __init__(self, name):
        self.name = name

    # 定义实例方法
    def start_game(self):
        print("%s开始游戏啦" % self.name)


# 1.查看帮助信息(调用静态方法)
Game.show_help()

# 2.查看历史最高分(调用类方法)
Game.show_top_score()

# 3.创建游戏对象(调用初始化方法)
game1 = Game("小明")

# 4.开始游戏(调用实例方法)
game1.start_game()

