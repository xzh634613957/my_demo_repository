"""
    根据错误类型捕获异常
"""
"""
    在程序执行时，可能会遇到 **不同类型的异常**，并且需要 **针对不同类型的异常，做出不同的响应**，这个时候，就需要捕获错误类型了
"""
"""
    try:
        # 尝试执行的代码
        pass
    except 错误类型1:
        # 针对错误类型1，对应的代码处理
        pass
    except (错误类型2, 错误类型3):
        # 针对错误类型2 和 3，对应的代码处理
        pass
    except Exception as result:
        print("未知错误 %s" % result)
"""
"""
    * 当 `Python` 解释器 **抛出异常** 时，**最后一行错误信息的第一个单词，就是错误类型**
"""
"""
    * 如果希望程序 **无论出现任何错误**，都不会因为 `Python` 解释器 **抛出异常而被终止**，可以再增加一个 `except`
    语法如下：
        except Exception as result:
            print("未知错误 %s" % result)
"""
"""
    **需求**
        1. 提示用户输入一个整数
        2. 使用 `8` 除以用户输入的整数并且输出
"""


try:
    num = int(input("请输入一个整数: "))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除0错误!")
except ValueError:
    print("请输入正确的整数!")
except Exception as a:
    print("未知错误: %s" % a)
