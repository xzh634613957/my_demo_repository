#!/usr/bin/env python2
# coding: utf-8

"""
    发布方实现: 发布小乌龟速度消息
        话题: /turtle1/cmd_vel
        消息: geometry_msgs/Twist
"""

import rospy
from geometry_msgs.msg import Twist


if __name__ =="__main__":
    rospy.init_node("my_control")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    # 组织数据并发布消息
    # 设置发布频率为 10 Hz
    rate = rospy.Rate(1)
    # 创建要发布的速度消息对象
    twist = Twist()
    # 设置发布的速度消息
    twist.linear.x = 2.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 2.0

    # 循环发布消息
    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()