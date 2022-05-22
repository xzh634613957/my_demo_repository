"""
    继承: 实现代码的复用, 相同的代码不需要重复的编写
"""
"""
    **重写** 父类方法有两种情况：
        1. **覆盖** 父类的方法
        2. 对父类方法进行 **扩展**
"""
"""
    * 如果在开发中，**子类的方法实现** 中 **包含** **父类的方法实现**
          * **父类原本封装的方法实现** 是 **子类方法的一部分**
    * 就可以使用 **扩展** 的方式
          1. **在子类中** **重写** 父类的方法
          2. 在需要的位置使用 `super().父类方法` 来调用父类方法的执行
          3. 代码其他的位置针对子类的需求，编写 **子类特有的代码实现**
"""


class Animal:
    def eat(self):
        print("吃东西")

    def drink(self):
        print("喝水")


class Dog(Animal):  # 继承
    def spoke(self):
        print("汪汪汪")


class XiaoTianQuan(Dog):
    def spoke(self):  # 重写父类方法(覆盖)
        print("-" * 50)
        print("我是神狗")


class XiaoTianQuan2(Dog):
    def spoke(self):  # 重写父类方法(扩展)
        print("-" * 50)
        super().spoke()  # 对父类中的方法进行扩展
        print("我也是神狗")



xiaobai = Dog()
xiaobai.drink()
xiaobai.spoke()

xiaotianquan = XiaoTianQuan()
xiaotianquan.spoke()

xiaotianquan2 = XiaoTianQuan2()
xiaotianquan2.spoke()
