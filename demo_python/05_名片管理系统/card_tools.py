# 所有名片相关的操作都要用到这个列表, 因此定义在程序的顶部
# 程序刚运行时没有数据, 因此是空列表
card_list = []  # 使用字典列表来记录每一张名片的详细信息


def show_menu():
    """
    名片管理系统的欢迎界面
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def card_add():
    """
    新增名片
    :return:None
    """
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入联系人姓名: ")
    while True:
        age_str = input("清输入联系人年龄: ")
        if age_str.isdigit():
            age_str = int(age_str)
            break
        else:
            print("请重新输入一个整数!")
    phone_str = input("请输入联系人电话: ")
    card_dict = {"name": name_str,
                 "age": age_str,
                 "phone": phone_str}
    card_list.append(card_dict)
    print("添加成功!")


def card_show():
    """
    显示所有名片
    :return:None
    """
    print("-" * 50)
    print("显示名片")
    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有名片, 请添加新名片!")
        return
    # 打印表头
    for name in ["序号", "姓名", "年龄", "电话"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    i = 1
    for show_dict in card_list:
        print("%d\t\t%s\t\t%d\t\t%s" % (i,
                                        show_dict["name"],
                                        show_dict["age"],
                                        show_dict["phone"]))
        i += 1


def card_search():
    """
    搜索名片
    :return: None
    """
    print("-" * 50)
    print("查询名片")
    name = input("清输入您要查找的姓名: ")
    for show_dict in card_list:
        if show_dict["name"] == name:
            for name in ["姓名", "年龄", "电话"]:
                print(name, end="\t\t\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t\t\t%d\t\t\t\t%s" % (show_dict["name"],
                                              show_dict["age"],
                                              show_dict["phone"]))
            # TODO 对名片进行修改和删除
            card_deal(show_dict)
            break
    else:
        print("没有这个人!")


def card_deal(find_dict):
    """
    修改或者删除查询到的名片
    :param find_dict:查询到的名片字典
    :return:None
    """
    while True:
        action = input("请选择要执行的操作: "
                       "[1]修改   [2]删除   [0]返回上级菜单\n")
        if action == "1":
            find_dict["name"] = input_card_info(find_dict["name"], "姓名(按回车取消修改): ")
            find_dict["age"] = int(input_card_info(find_dict["age"], "年龄(按回车取消修改): "))
            find_dict["phone"] = input_card_info(find_dict["phone"], "电话(按回车取消修改): ")
            print("修改成功!")
            return
        elif action == "2":
            card_list.remove(find_dict)
            print("删除成功!")
            return
        elif action == "0":
            return
        else:
            print("输入错误, 请重新输入!")


def input_card_info(dict_value, tip_message):
    """
    输入修改后的名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示信息
    :return:如果用户输入了内容就返回内容,否则返回字典中原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
