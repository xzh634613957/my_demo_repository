"""
练习1: if else的使用
"""
print("-" * 10 + "练习1: if else的使用" + "-" * 10)
# 1.定义一个整数变量记录年龄
age = 17
# 2.判断是否满了18岁
if age >= 18:
    # 3.如果满了18岁,则可以进网吧嗨皮
    print("可以进网吧嗨皮")
else:
    print("未成年人禁止入内!")

"""
练习2: elif 的使用
1. 定义 `holiday_name` 字符串变量记录节日名称
2. 如果是 **情人节** 应该 **买玫瑰**／**看电影**
3. 如果是 **平安夜** 应该 **买苹果**／**吃大餐**
4. 如果是 **生日** 应该 **买蛋糕**
5. 其他的日子每天都是节日啊……
"""
print("\n")
print("-" * 10 + "练习2: elif 的使用" + "-" * 10)
holiday_name = "情人节"
if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("其他的日子每天都是节日")

"""
练习3: if嵌套的使用
1. 定义布尔型变量 `has_ticket` 表示是否有车票
2. 定义整型变量 `knife_length` 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 **安检**
4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
   * 如果超过 20 厘米，提示刀的长度，不允许上车
   * 如果不超过 20 厘米，安检通过
5. 如果没有车票，不允许进门
"""
print("\n")
print("-" * 10 + "练习3: if嵌套的使用" + "-" * 10)
has_ticket = True
knife_length = 20.5
if has_ticket:
    print("有车票,可以进行安检")
    if knife_length > 20:
        print("您的刀为%.2f厘米, 不允许上车" % knife_length)
    else:
        print("安检通过")
else:
    print("没有车票,不允许进门")
