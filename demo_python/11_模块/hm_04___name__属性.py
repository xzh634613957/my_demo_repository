"""
    __name__ 属性
"""
"""
    * 一个 **独立的 `Python` 文件** 就是一个 **模块**
    * 在导入文件时，文件中 **所有没有任何缩进的代码** 都会被执行一遍！
"""
"""
    **实际开发场景**
        * 在实际开发中，每一个模块都是独立开发的，大多都有专人负责
        * **开发人员** 通常会在 **模块下方** **增加一些测试代码**
            * 仅在模块内使用，而被导入到其他文件中不需要执行
"""
"""
    `__name__` 属性
        * `__name__` 属性可以做到，测试模块的代码 **只在测试情况下被运行**，而在 **被导入时不会被执行**！
        * `__name__` 是 `Python` 的一个内置属性，记录着一个 **字符串**
            * 如果 **是被其他文件导入的**，`__name__` 就是 **模块名**
            * 如果 **是当前执行的程序** `__name__` 是 **`__main__`**
"""
"""
    **在很多 `Python` 文件中都会看到以下格式的代码**：
        # 导入模块
        # 定义全局变量
        # 定义类
        # 定义函数
        
        # 在代码的最下方调用主函数
        def main():
            # ...
            pass
        
        # 根据 __name__ 判断是否执行下方代码
        if __name__ == "__main__":
            main()
"""