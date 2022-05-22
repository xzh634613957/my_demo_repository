"""
    break 在某一条件满足时, 退出循环, 不再执行后续重复的代码
    continue 在某一条件满足时, 不执行后续重复的代码, 但是不退出循环
"""

i = 0
while i < 10:
    if i == 5:
        break
    i += 1
    print(i)

j = 10
while j < 20:
    if j == 15:
        j += 1
        continue
    j += 1
    print(j)
