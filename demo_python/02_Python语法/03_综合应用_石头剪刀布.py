"""
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 **随机** 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负
"""
# 使用随机数,需要导入随机数的工具包
# 导入工具包的时候,应该将导入的语句放在文件的顶部
import random

# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入您要出的拳(石头-1/剪刀-2／布-3): "))
# 2. 电脑 **随机** 出拳
computer = random.randint(1, 3)  # random.randint(a, b)返回[a,b]之间的整数
print("您选择的拳是 %d, 电脑选择的拳是 %d" % (player, computer))
# 3. 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("您真的太厉害了耶~")
elif player == computer:
    print("平局哦~")
else:
    print("您输了哦~")
