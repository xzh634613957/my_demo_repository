"""
    * Python 中数据类型可以分为 **数字型** 和 **非数字型**
    * 数字型
      * 整型 (`int`)
      * 浮点型（`float`）
      * 布尔型（`bool`）
        * 真 `True` `非 0 数` —— **非零即真**
        * 假 `False` `0`
      * 复数型 (`complex`)
        * 主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
    * 非数字型
      * 字符串
      * 列表
      * 元组
      * 字典

    * 在 `Python` 中，所有 **非数字型变量** 都支持以下特点：
      1. 都是一个 **序列** `sequence`，也可以理解为 **容器**
      2. **取值** `[]`
      3. **遍历** `for in`
      4. **计算长度**、**最大/最小值**、**比较**、**删除**
      5. **链接** `+` 和 **重复** `*`
      6. **切片**
"""

"""
    * `List`（列表） 是 `Python` 中使用 **最频繁** 的数据类型，在其他语言中通常叫做 **数组**
    * 专门用于存储 **一串 信息**, 可以是数据类型各不相同的一串数据
    * 列表用 `[]` 定义，**数据** 之间使用 `,` 分隔
    * 列表的 **索引** 从 `0` 开始
      * **索引** 就是数据在 **列表** 中的位置编号，**索引** 又可以被称为 **下标**
    
    > 注意：从列表中取值时，如果 **超出索引范围**，程序会报错
"""
name_list1 = []  # 定义一个空列表
temp_list = ["小李", "小周"]
name_list = ["小明", "小李", "小豪"]

# 1.取值
print(name_list[0], name_list[1], name_list[2])

# 2.索引 (知道列表中的内容, 想确定数据在列表中的位置)
print(name_list.index("小李"))

# 3.修改
name_list[1] = "小熊"

# 4.增加
name_list.append("小志")  # 在列表末尾追加一个数据
name_list.insert(4, "小谢")  # 在指定索引位置插入数据
name_list.extend(temp_list)  # 将另一个列表的所有数据追加到该列表的末尾

# 5.删除
name_list.remove("小明")  # 从列表中删除指定的数据, 若有重复的数据, 则删除第一个
name_list.pop()  # 默认删除列表中的最后一个数据
name_list.pop(3)  # 删除列表中指定索引的数据
del name_list[1]  # 删除列表中指定索引的数据 (del的本质是用来将一个变量从内存中删除, 不建议用来删除列表中的数据)
name_list.clear()  # 清空列表中的所有内容

print(name_list)

# 6.统计
name_list2 = ["小熊", "小志", "小豪", "小豪"]
len(name_list2)  # 统计列表中元素的总数
name_list2.count("小豪")  # 统计列表中指定数据出现的次数

# 7.排序
num_list = [2, 5, 6, 1, 23, 5]
# num_list.sort()  # 对列表进行升序排列
# name_list2.sort()  # 中文按照笔画排列
# num_list.sort(reverse=True)  # 对列表进行降序排列
num_list.reverse()  # 对列表中的内容进行翻转(逆序)

print(num_list)
print(name_list2)





