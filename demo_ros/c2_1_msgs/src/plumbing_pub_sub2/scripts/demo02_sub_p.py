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

# 1.导包
import rospy
from std_msgs.msg import String

# 4.回调函数处理数据
def doMsg(msg):
    rospy.loginfo("订阅数据: %s" % msg.data)

if __name__ == "__main__":
    # 2.初始化ROS节点
    rospy.init_node("listener")
    # 3.创建订阅者对象
    sub = rospy.Subscriber("chatter",String,doMsg,queue_size=10)
    # 4.回调函数处理数据
    # 5.spin()调用回调函数
    rospy.spin()
