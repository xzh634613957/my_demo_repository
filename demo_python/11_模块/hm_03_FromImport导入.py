"""
    from...import 导入
"""
"""
    * 如果希望 **从某一个模块** 中，导入 **部分** 工具，就可以使用 `from ... import` 的方式
    * `import 模块名` 是 **一次性** 把模块中 **所有工具全部导入**，并且通过 **模块名/别名** 访问
"""
"""
    语法:
        from 模块名 import 工具名
"""
"""
    from...import 导入之后
        * **不需要** 通过 `模块名.`
        * 可以直接使用 **模块提供的工具** —— **全局变量**、**函数**、**类**
"""
"""
    **注意**
        > 如果 **两个模块**，存在 **同名的函数**，那么 **后导入模块的函数**，会 **覆盖掉先导入的函数**
        * 开发时 `import` 代码应该统一写在 **代码的顶部**，更容易及时发现冲突
        * 一旦发现冲突，可以使用 `as` 关键字 **给其中一个工具起一个别名**
"""
"""
    from...import *
        从 模块 导入 所有工具
        这种方式不推荐使用，因为函数重名并没有任何的提示，出现问题不好排查
"""

from hm_01_测试模块1 import Dog
from hm_01_测试模块2 import say_hello


# 不需要通过 `模块名.`来调用模块里的工具
wangcai = Dog()
print(wangcai)

say_hello()

