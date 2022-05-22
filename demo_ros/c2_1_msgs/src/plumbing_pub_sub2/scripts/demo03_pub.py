#! /usr/bin/env python
#coding:utf-8

import rospy
from plumbing_pub_sub2.msg import Person

"""
    发布方: 发布人的消息
        1.导包
        2.初始化ROS节点
        3.创建发布者对象
        4.组织发布逻辑并发布数据
            4.1 创建消息对象
            4.2 创建发布频率对象
            4.2 循环发布消息
"""

if __name__ == "__main__":
    rospy.init_node("talker_person")

    pub = rospy.Publisher("chatter_person",Person,queue_size=10)
   
    p = Person()
    p.name = "葫芦娃"
    p.age = 18
    p.height = 1.75

    rate = rospy.Rate(1)

    rospy.sleep(2)

    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布的消息为: 姓名: %s, 年龄: %d岁, 身高: %.2f米" % (p.name, p.age, p.height))
        rate.sleep()

