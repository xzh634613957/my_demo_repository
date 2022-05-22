"""
    使用 `as` 指定模块的别名
        **如果模块的名字太长**，可以使用 `as` 指定模块的名称，以方便在代码中的使用
"""
"""
    注意：**模块别名** 应该符合 **大驼峰命名法**
"""


import hm_01_测试模块1 as TestDog
import hm_01_测试模块2 as TestCat


print(TestDog.title)
print(TestCat.title)

TestDog.say_hello()
TestCat.say_hello()

dog = TestDog.Dog()
print(dog)
cat = TestCat.Cat()
print(cat)
