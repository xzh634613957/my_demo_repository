"""
    1. 有连个整型变量 a = 6, b = 100
    2. 不适用其他变量, 交换两个变量的值
"""

"""
    解法1: 使用其他变量
"""

gl_a = 6
gl_b = 100


def swap(a, b):
    c = a
    a = b
    b = c
    return a, b


gl_a, gl_b = swap(gl_a, gl_b)
print(gl_a, gl_b)

"""
    解法2: 不使用其他变量
"""
gl_a = gl_a + gl_b
gl_b = gl_a - gl_b
gl_a = gl_a - gl_b
print(gl_a, gl_b)

"""
    解法3: Python专有解法---元组
"""
gl_a, gl_b = (gl_b, gl_a)  # 右边的小括号可以省略
print(gl_a, gl_b)

