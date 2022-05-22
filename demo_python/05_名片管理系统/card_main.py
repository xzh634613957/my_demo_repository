#! /usr/bin/env python3

"""
    需求:
    * 1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单

    **************************************************
    欢迎使用【名片管理系统】V1.0

    1. 新建名片
    2. 显示全部
    3. 查询名片

    0. 退出系统
    **************************************************

    * 2. 用户用数字选择不同的功能
    * 3. 根据功能选择，执行不同的功能
    * 4. 用户名片需要记录用户的 **姓名**、**电话**、**QQ**、**邮件**
    * 5. 如果查询到指定的名片，用户可以选择 **修改** 或者 **删除** 名片
"""

import card_tools

"""
    步骤:
        1. 框架搭建
        2. 显示功能菜单, 退出系统
        3. 新建名片
        4. 显示全部名片
        5. 查询名片后修改/删除名片
"""

while True:
    # 欢迎界面
    card_tools.show_menu()
    # 选择界面
    action = input("请选择操作功能: ")
    if action == "0":
        card_exit = input("是否确定退出系统? 是(Y)/否(N): ")
        if card_exit == "Y":
            print("感谢您的使用,再见!")
            break
        elif card_exit == "N":
            continue
        else:
            print("输入错误,请重新输入!")
    elif action in ["1", "2", "3"]:
        if action == "1":
            card_tools.card_add()
        elif action == "2":
            card_tools.card_show()
        else:
            card_tools.card_search()
    else:
        print("输入错误,请重新输入!")
