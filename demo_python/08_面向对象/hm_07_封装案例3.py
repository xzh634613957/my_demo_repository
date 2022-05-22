"""
    士兵突击案例
"""
"""
    重点: 
        * 类创建的对象可以是另一个类的属性
        * 在定义类的属性时. 如果不知道设置什么初始值, 可以设置为 None
"""
"""
    **需求**
        1. **士兵** **许三多** 有一把 **AK47**
        2. **士兵** 可以 **开火**
        3. **枪** 能够 **发射** 子弹
        4. **枪** 装填 **装填子弹** —— **增加子弹数量**
"""


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹, 无法射击")
            return
        self.bullet_count -= 1
        # print("[%s]发射子弹, 剩余[%d]颗子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        self.gun.add_bullet(50)
        self.gun.shoot()
        print("[%s]举起了他的[%s], 还剩[%d]颗子弹" % (self.name, self.gun.model, self.gun.bullet_count))



gun1 = Gun("AK47")
# gun1.add_bullet(100)

xusanduo = Soldier("许三多")
xusanduo.gun = gun1
xusanduo.fire()
