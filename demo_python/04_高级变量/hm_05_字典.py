"""
    * `dictionary`（字典） 是 **除列表以外** `Python` 之中 **最灵活** 的数据类型
    * 字典同样可以用来 **存储多个数据**
        * 通常用于存储 **描述一个 `物体` 的相关信息**
    * 和列表的区别
        * **列表** 是 **有序** 的对象集合
        * **字典** 是 **无序** 的对象集合
    * 字典用 `{}` 定义
    * 字典使用 **键值对** 存储数据，键值对之间使用 `,` 分隔
        * **键** `key` 是索引
        * **值** `value` 是数据
        * **键** 和 **值** 之间使用 `:` 分隔
        * **键必须是唯一的**
        * **值** 可以取任何数据类型，但 **键** 只能使用 **字符串**、**数字**或 **元组**
"""

xiaoMing = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.78,
            "weight": 70}
print("原始字典:xiaoMing =", xiaoMing)

# 1.取值
print("取值:", xiaoMing["gender"])
# 2.增加/修改
xiaoMing["haoJiYou"] = "小李"
print("增加: xiaoMing =", xiaoMing)
xiaoMing["name"] = "小小明"
print("修改: xiaoMing =", xiaoMing)
# 3.删除
# print("删除: xiaoMing =", xiaoMing.pop("haoJiYou"))
xiaoMing.pop("haoJiYou")
print("删除: xiaoMing =", xiaoMing)
# 4.统计键值对数量
print("取长: xiaoMing的长度为: ", len(xiaoMing))
# 5.合并字典
temp = {"父亲": "王炸",
        "母亲": "球球",
        "age": 20}
xiaoMing.update(temp)
print("合并: xiaoMing =", xiaoMing)
# 6.清空字典
xiaoMing.clear()
print("清空: xiaoMing =", xiaoMing)

