"""
    * 定义函数时，可以给 **某个参数** 指定一个**默认值**，具有默认值的参数就叫做 **缺省参数**
    * 调用函数时，如果没有传入 **缺省参数** 的值，则在函数内部使用定义函数时指定的 **参数默认值**
    * 函数的缺省参数，**将常见的值设置为参数的缺省值**，从而 **简化函数的调用**
    * 例如：对列表排序的方法
"""

"""
    示例1: 列表排序方法的缺省参数
"""
gl_list = [1, 4, 2, 5]
# 列表的排序方法默认为升序, sort方法的三个参数均为缺省参数
gl_list.sort()
print(gl_list)
# reverse 的默认值为 False
gl_list.sort(reverse=True)
print(gl_list)

"""
    示例2: 指定函数缺省参数的默认值
"""


def print_info(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s" % (name, gender_text))


print_info("小明")
print_info("小美", False)
