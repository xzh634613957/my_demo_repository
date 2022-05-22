#! /usr/bin/env python
# coding: utf-8

"""
    需求:
        现有坐标系统，父级坐标系统 world,下有两子级系统 son1(turtle1)，son2(turtle2)，
        son1 相对于 world，以及 son2 相对于 world 的关系是已知的(tf04_pub_turtle节点在广播这个信息)，
        求 son1 与 son2 中的坐标关系, 并生成 turtle2 的速度控制信息, 然后发布
"""
"""
    实现流程:
        1.导包
        2.初始化节点
        3.创建订阅对象
        4.调用API(lookup_transform)求出son1相对于son2的坐标关系
        5.生成速度信息, 然后发布
        6.spin()
"""

# 1.导包
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped, Twist
import math


if __name__ == "__main__":
    
    # 2.初始化节点
    rospy.init_node("control_turtle")

    # 3.创建订阅对象
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)

    rate = rospy.Rate(1)

    # 4.调用API(lookup_transform)求出turtle1相对于turtle2的坐标关系(其实就是在求位置误差)
    # 4.1 创建速度信息发布者对象
    pub = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=100)
    """
        参数1: 话题名称(使用 rostopic list 查看)
        参数2: 消息类型(使用 rostopic info /turtle2/cmd_vel 查看)
    """
    """
        geometry_msgs/Twist 消息格式(使用 rosmsg info geometry_msgs/Twist 查看):
            geometry_msgs/Vector3 linear
                float64 x
                float64 y
                float64 z
            geometry_msgs/Vector3 angular
                float64 x
                float64 y
                float64 z

    """

    while not rospy.is_shutdown():
        try:
            # 4.2 求出turtle1相对于turtle2的坐标关系
            ts = buffer.lookup_transform("turtle2", "turtle1", rospy.Time(0))
            """
                API: lookup_transform(参数1, 参数2, 参数3)
                参数1: 目标坐标系
                参数2: 原坐标系
                参数3: 时间关系
                返回值: 原坐标系与目标坐标系的关系
            """
            rospy.loginfo("son1与son2的相对关系:")
            rospy.loginfo("父级坐标系: %s", ts.header.frame_id)
            rospy.loginfo("子级坐标系: %s", ts.child_frame_id)
            rospy.loginfo("相对坐标: x=%.2f, y=%.2f, z=%.2f",
                            ts.transform.translation.x,
                            ts.transform.translation.y,
                            ts.transform.translation.z)

            # 5.生成线速度和角速度控制信息(根据 Twist 的消息格式), 然后发布给 turtle2
            # 5.1 创建发布者需要发布的消息对象
            twist = Twist()

            # 5.2 根据算法计算出线速度和角速度信息(乌龟GUI中只需要 x方向上的线速度 和 z方向上的角速度)
            # 5.2.1 线速度 = 比例系数 * 位置误差
            twist.linear.x = 0.5 * math.sqrt(math.pow(ts.transform.translation.x, 2) + 
                                             math.pow(ts.transform.translation.y, 2))
            # 5.2.1 角速度 = 比例系数 * 角度误差
            twist.angular.z = 1.2 * math.atan2(ts.transform.translation.y, ts.transform.translation.x)

            # 5.3 发布者发布消息
            pub.publish(twist)

        except Exception as e:
            rospy.logwarn("错误提示: %s" % e)

        rate.sleep()

    # 5.spin()
