"""
    练习1: while语法
"""
print("-" * 10 + "练习1: while循环的语法" + "-" * 10)
i = 0
while i < 10:
    i += 1
    char = "Hello Python" + str(i)
    print(char)
print("-" * 10 + "练习1: while循环的语法" + "-" * 10)

"""
练习2: 计算 0 ~ 100 之间所有偶数的累计求和结果
"""
print("-" * 10 + "练习2: 计算求和" + "-" * 10)
i = 0
add = 0
while i <= 100:
    if i % 2 == 0:
        add += i
    i += 1
print("0+2+...+100=%d" % add)
print("-" * 10 + "练习2: 计算求和" + "-" * 10)



