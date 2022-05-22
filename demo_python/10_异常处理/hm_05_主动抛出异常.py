"""
    主动抛出异常
"""
"""
    * `Python` 中提供了一个 `Exception` **异常类**
    * 在开发时，如果满足 **特定业务需求时**，希望 **抛出异常**，可以：
          1. **创建** 一个 `Exception` 的 **对象**
          2. 使用 `raise` **关键字** 抛出 **异常对象**
"""
"""
    **需求**
        * 定义 `input_password` 函数，提示用户输入密码
        * 如果用户输入长度 < 8，抛出异常
        * 如果用户输入长度 >=8，返回输入的密码
"""


def input_password():

    # 1.提示用户输入密码
    pwd = input("请输入密码: ")

    # 2.判断用户输入的密码长度, 如果 >=6, 则返回用户输入的密码
    if len(pwd) >= 6:
        return pwd

    # 3.如果密码长度不够, 则抛出异常
    # 3.1 创建异常对象, 使用异常的错误信息字符串作为参数
    err = Exception("密码长度不够")  # Exception也是一个类

    # 3.2 抛出异常对象
    raise err


# 在主函数中使用try捕获异常
try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print("输入错误: %s" % result)

