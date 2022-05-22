"""
    eval函数
"""
"""
    `eval()` 函数十分强大 —— **将字符串** 当成 **有效的表达式** 来求值 并 **返回计算结果**
"""
"""
    # 基本的数学计算
    In [1]: eval("1 + 1")
    Out[1]: 2
    
    # 字符串重复
    In [2]: eval("'*' * 10")
    Out[2]: '**********'
    
    # 将字符串转换成列表
    In [3]: type(eval("[1, 2, 3, 4, 5]"))
    Out[3]: list
    
    # 将字符串转换成字典
    In [4]: type(eval("{'name': 'xiaoming', 'age': 18}"))
    Out[4]: dict
"""
"""
    案例: 计算器
"""


input_str = input("请输入一个算数题: ")
print(eval(input_str))
