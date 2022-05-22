#! /usr/bin/env python
# coding: utf-8

# 1.导包
import rospy
import rosbag
from std_msgs.msg import String

"""
    需求: 写出消息数据到磁盘上的 bag 文件
    流程:
        1.导包
        2.初始化节点
        3.创建 rosbag 对象并打开文件流
        4.写数据
        5.关闭文件流
"""


if __name__ == "__main__":

    # 2.初始化节点
    rospy.init_node("write_bag")

    # 3.创建 rosbag 对象并打开文件流
    bag = rosbag.Bag("/home/xiongzh/demo_ros/c5_2_rosbag/src/rosbag_demo/test.bag", 'w')
    """
        参数1: 保存的 bag 文件路径
        参数2: 'w' --- 写; 'r' --- 读 
    """
    # 4.写数据
    # 4.1 创建消息对象
    msg = String()
    msg.data = "hello_bag"
    # 4.2 写入数据
    bag.write("topic", msg)
    bag.write("topic", msg)
    bag.write("topic", msg)
    bag.write("topic", msg)
    bag.write("topic", msg)
    bag.write("topic", msg)

    # 5.关闭文件流
    bag.close()

