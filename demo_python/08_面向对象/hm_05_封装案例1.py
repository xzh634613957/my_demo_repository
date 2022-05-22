"""
    面向对象封装案例1: 小明爱跑步
"""
"""
    封装是面向对象编程的一大特点
        * 面向对象编程的第一步: 将属性和方法封装到一个抽象的类中
        * 外界使用类创建对象, 然后让对象调用方法
        * 对象方法的细节都被封装在类的内部
        * 在对象的方法的内部, 可以直接访问对象的属性
"""
"""
    需求:
        * 小明体重75.0公斤
        * 小明每次跑步都会减肥0.5公斤
        * 小明每次吃东西体重增加1公斤
"""
"""
    分析: 
        * 属性: 小明, 体重
        * 方法: 跑步, 吃东西
"""


class Person:
    def __init__(self, name, weight, gender=True):
        self.name = name
        self.weight = weight
        if gender:
            self.gender = "男生"
        else:
            self.gender = "女生"

    def __str__(self):
        return "%s是%s, ta的体重为: %.2f公斤" % (self.name, self.gender, self.weight)

    def run(self):
        self.weight = self.weight - 0.5

    def eat(self):
        self.weight = self.weight + 1


xiaoming = Person("小明", 75, gender=False)
print(xiaoming)

xiaoming.eat()
print(xiaoming)

xiaoming.run()
print(xiaoming)
