#! /usr/bin/env python
#coding:utf-8

"""
    使用Python实现订阅消息:
        1.导包
        2.初始化ROS节点
        3.创建订阅者对象
        4.回调函数处理数据
        5.spin()调用回调函数
"""

import rospy
from plumbing_pub_sub2.msg import Person

def doMsg_p(p):
    rospy.loginfo("收到的消息--- 姓名: %s  年龄: %d  身高: %.2f", p.name, p.age, p.height)


if __name__ == "__main__":
    rospy.init_node("listener_person")

    sub = rospy.Subscriber("chatter_person",Person,doMsg_p,queue_size=10)

    rospy.spin()
