"""
    * 使用 `list` 函数可以把元组转换成列表
    * 使用 `tuple` 函数可以把列表转换成元组
"""

num_list = [1, 4, 5]
num_tuple = tuple(num_list)
print(num_tuple)
num_list_new = list(num_tuple)
print(num_list_new)
