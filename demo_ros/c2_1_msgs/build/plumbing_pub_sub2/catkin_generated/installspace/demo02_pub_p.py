#!/usr/bin/env python2
#coding:utf-8

"""
    使用Python实现消息发布:
        1.导包
        2.初始化ROS节点
        3.创建发布者对象
        4.编写发布逻辑并发布数据
"""
# 1.导包
import rospy
from std_msgs.msg import String  # 发布的消息的数据类型

if __name__ == "__main__":
        # 2.初始化ROS节点
        rospy.init_node("talker")
        # 3.创建发布者对象
        pub = rospy.Publisher("chatter",String,queue_size=10)
        # 4.编写发布逻辑并发布数据
        # 创建发布的消息对象
        msg = String()
        msg_front = "Hello World"
        count = 0  # 设置计数器
        rate = rospy.Rate(1)  # 设置循环频率 1 Hz
        rospy.sleep(3)  # 先休眠 3 s
        # 使用循环发布数据
        while not rospy.is_shutdown():
            # 在循环中发布数据
            msg.data = msg_front + str(count)
            pub.publish(msg)
            rate.sleep()
            rospy.loginfo("写出的数据: %s" % msg.data)
            count += 1
