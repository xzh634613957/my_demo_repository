def sum_2_num(num1, num2):
    """
    对两个数相加并打印出来
    :param num1:
    :param num2:
    :return:
    """
    result = num1 + num2
    print("改前: %d + %d = %d" % (num1, num2, result))
    num1 = 20
    num2 = 30
    result = num1 + num2
    print("改后: %d + %d = %d" % (num1, num2, result))
    return result


print(sum_2_num(10, 20))
