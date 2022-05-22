#! /usr/bin/env python
#coding:utf-8

"""
    演示参数服务器上参数的新增与修改
    需求: 在参数服务器中设置机器人的型号与半径
    实现: rospy.set_param()

"""
import rospy


if __name__ == "__main__":
    rospy.init_node("para_set")

    rospy.set_param("type", "xiaohuangche")
    rospy.set_param("radius", 14)
