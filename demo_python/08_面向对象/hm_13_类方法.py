"""
    类方法
"""
"""
    * **类方法** 就是针对 **类对象** 定义的方法
          * 在 **类方法** 内部可以直接访问 **类属性** 或者调用其他的 **类方法**
"""
"""
    类方法需要用 **修饰器** `@classmethod` 来标识，**告诉解释器这是一个类方法**
"""
"""
    类方法的 **第一个参数** 应该是 `cls`(class)
        * 由 **哪一个类** 调用的方法，方法内的 `cls` 就是 **哪一个类的引用**
        * 这个参数和 **实例方法** 的第一个参数是 `self` 类似
        * **提示** 使用其他名称也可以，不过习惯使用 `cls`
"""
"""
    **在方法内部**
        * 可以通过 `cls.` **访问类的属性**
        * 也可以通过 `cls.` **调用其他的类方法**
"""


class Tool(object):

    # 定义类属性
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        # print(Tool.count)
        print(cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")

# 调用类方法
Tool.show_tool_count()
