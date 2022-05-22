#! /usr/bin/env python
# coding: utf-8

# 1.导包
import rospy
import rosbag



"""
    需求: 读取磁盘上的 bag 文件
    流程:
        1.导包
        2.初始化节点
        3.创建 rosbag 对象并打开文件流
        4.读数据
        5.关闭文件流
"""


if __name__ == "__main__":

    # 2.初始化节点
    rospy.init_node("read_bag")

    # 3.创建 rosbag 对象并打开文件流
    bag = rosbag.Bag("/home/xiongzh/demo_ros/c5_2_rosbag/src/rosbag_demo/test.bag", 'r')

    # 4.读数据
    msgs = bag.read_messages("topic")
    # 4.1 遍历读取msgs中的数据
    for topic, msg, time in msgs:
        rospy.loginfo("话题:%s, 消息:%s, 时间:%s" 
                        % (topic, msg.data, time))
    
    # 5.关闭文件流
    bag.close()

