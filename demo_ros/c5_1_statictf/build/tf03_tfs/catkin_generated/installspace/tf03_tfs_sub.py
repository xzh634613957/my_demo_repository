#!/usr/bin/env python2
# coding: utf-8

"""
    需求:
        现有坐标系统，父级坐标系统 world,下有两子级系统 son1，son2，
        son1 相对于 world，以及 son2 相对于 world 的关系是已知的，
        求 son1 与 son2中的坐标关系，又已知在 son1中一点的坐标，要求求出该点在 son2 中的坐标
"""
"""
    实现流程:
        1.导包
        2.初始化节点
        3.创建订阅对象
        4.调用API(lookup_transform)求出son1相对于son2的坐标关系
        5.创建依赖于son1的坐标点, 调用API(transform)求出该点在son2中的坐标
        6.spin()
"""

# 1.导包
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf2_geometry_msgs import PointStamped


if __name__ == "__main__":

    # 2.初始化节点(需要导入rospy)
    rospy.init_node("frames_sub")

    # 3.创建订阅对象(需要导入tf2_ros)
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
    
    # 4.调用API(lookup_transform)求出son1相对于son2的坐标关系
        try:
            ts = buffer.lookup_transform("son2", "son1", rospy.Time(0))
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
                            
    # 5.创建依赖于son1的坐标点, 调用API(transform)求出该点在son2中的坐标
            ps = PointStamped()
            ps.header.frame_id = "son1"
            ps.header.stamp = rospy.Time.now()
            ps.point.x = 1.0
            ps.point.y = 1.0
            ps.point.z = 1.0

            ps_out = buffer.transform(ps, "son2", rospy.Duration(0.5))
            
            rospy.loginfo("ps所处的坐标系为: %s", ps.header.frame_id)
            rospy.loginfo("ps相对于 son2 的坐标为: (%.2f, %.2f, %.2f)",
                            ps_out.point.x,
                            ps_out.point.y,
                            ps_out.point.z)

        except Exception as e:
            rospy.logerr("错误提示: %s", e)

        rate.sleep()
    
    # 6.spin()


    

