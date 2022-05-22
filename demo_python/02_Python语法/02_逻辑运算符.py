"""
Python中的逻辑运算符包括:
    and --- 与
    or  --- 或
    not --- 非
"""

"""
练习1: 定义一个整数变量 `age`，编写代码判断年龄是否正确
* 要求人的年龄在 0-120 之间
"""
age = 120
if age > 0 and age < 120:  # 也可以用 and: if 0 < age < 120
    print("您今年为%d岁." % age)
else:
    print("请输入正确的年龄!")

"""
练习2: 定义两个整数变量 `python_score`、`c_score`，编写代码判断成绩
   * 要求只要有一门成绩 > 60 分就算合格
"""
python_score = 60
c_score = 50
if python_score > 60 or c_score > 60:
    print("成绩合格")
else:
    print("成绩不合格")

"""
练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
   * 如果不是提示不允许入内
"""
is_employee = False
if not is_employee:
    print("请勿进入")