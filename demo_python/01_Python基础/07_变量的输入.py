# 在python中, 如果要获取用户通过键盘输入的信息, 需要使用 input() 函数

password = input("请输入银行密码: ")
passwordInt = int(password)
passwordFlo = float(password)
print("确认您的密码: ", passwordInt)

"""
注意:
    1.input()函数输出的类型是字符串
    2.用户输入的任何内容Python都认为是一个字符串
    3.int(x), float(x)可以将x转换为整数或浮点数
"""