"""
    定义类
"""
"""
    语法:
        # 创建类 
        class 类名:
            def 方法(self, 参数列表):
                pass
        
        # 创建对象
        对象变量 = 类名()
"""


# case1 创建类和对象
class Cat:
    def eat(self):  # self相当于 this 指针
        print("小猫爱吃鱼")

    def drink(self):
        print("%s要喝水" % self.name)


cat = Cat()
cat.eat()

# case2 给对象增加属性
"""
    在Python中给对象设置属性非常容易,但是并不推荐使用这种方式设置
    因为对象属性的封装应该封装在类的内部 
"""
cat.name = "Tom"  # 在需要在类的外部代码中直接通过 . 设置一个属性即可

print(cat)

# case3 类中方法里的self
"""
    * 类中方法里的self相当于this指针
    * 哪一个对象调用的方法,self就是哪一个对象的引用
    * 在调用方法时不需要传递self的参数
    * 在方法内部
        - 可以通过 self. 来访问该对象的属性
        - 也可以通过 self. 来调用该对象的其他方法
"""
cat2 = Cat()
cat2.name = "Tom2"
cat2.drink()


