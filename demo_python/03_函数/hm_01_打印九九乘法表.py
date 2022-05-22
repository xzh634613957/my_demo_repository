def multiple_table():
    """
    def 是define的缩写
    :return:0
    """
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            product = j * i
            print("%d×%d=%d" % (i, j, product), end="\t")
            j += 1
        print()
        i += 1


multiple_table()
