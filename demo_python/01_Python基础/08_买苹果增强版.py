"""
需求:
    1.收银员输入苹果的价格, 单位: 元/斤
    2.收银员输入用户购买苹果的数量, 单位: 斤
    3.计算并且输出付款金额
"""

price = float(input("请输入苹果的价格: "))  # 嵌套函数
weight = float(input("请输入苹果的重量: "))
print("应付金额为: %.02f" % (price * weight))

"""
格式化字符(包含%的字符串,输出文字信息的同时输出数据):
    %s -----  字符串
    %d -----  有符号十进制整数
    %06d ---  表示输出整数的显示位数, 不足的地方用0补全
    %f -----  浮点数
    %.02f --  表示小数点后只显示两位
    %% -----  输出 %
语法: 
    a.print("格式化字符串" % 变量)
    b.print("格式化字符串" % (变量1, 变量2...))   
"""