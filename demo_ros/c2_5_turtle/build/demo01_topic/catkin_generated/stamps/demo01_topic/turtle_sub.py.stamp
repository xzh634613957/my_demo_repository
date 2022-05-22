#! /usr/bin/env python
# coding: utf-8

"""
    订阅方实现: 订阅小乌龟的位姿信息
        话题: /turtle1/pose (使用 rostopic list 查看) 
        消息: turtlesim/Pose (使用 rostopic info /turtle1/pose)
        消息类型: (使用 rosmsg info turtlesim/Pose)
                float32 x
                float32 y
                float32 theta
                float32 linear_velocity
                float32 angular_velocity
"""

import rospy
from turtlesim.msg import Pose

def doPose(data):
    rospy.loginfo("小乌龟当前的坐标为: (%.2f,%.2f), 角度: theta=%.2f" % (data.x, data.y, data.theta))
    rospy.loginfo("线速度: %.2f m/s" % data.linear_velocity)
    rospy.loginfo("角速度: %.2f rad/s" % data.angular_velocity)



if __name__ == "__main__":
    rospy.init_node("turtle_pose")
    sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=10)
    rospy.spin()
