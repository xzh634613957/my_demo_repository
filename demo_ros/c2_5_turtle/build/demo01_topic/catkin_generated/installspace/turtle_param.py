#!/usr/bin/env python2
# coding: utf-8

"""
    需求: 修改参数服务器上小乌龟GUI的背景颜色
        参数服务器参数: (rosparam list)
                    /turtlesim/background_b
                    /turtlesim/background_g
                    /turtlesim/background_r
"""

import rospy


if __name__ == "__main__":
    rospy.init_node("turtle_param_set")
    
    rospy.set_param("/turtlesim/background_r",255)
    rospy.set_param("/turtlesim/background_g",20)
    rospy.set_param("/turtlesim/background_b",20)
    rospy.loginfo("颜色设置成功~")
