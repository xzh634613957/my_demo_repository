#! /usr/bin/env python
#coding:utf-8

"""
    获取参数服务器中的参数
    rospy.get_param("参数名", 参数默认值)
    rospy.get_param_cached("参数名")
    rospy.get_param_names()
    rospy.has_param("参数名")
    rospy.search_param("参数名")
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("para_get")

    type_g = rospy.get_param("type", "small_car")
    type_g1 = rospy.get_param("type_p", "small_car")

    type_g2 = rospy.get_param_cached("type")

    rospy.loginfo("type_g = %s" % type_g)
    rospy.loginfo("type_g1 = %s" % type_g1)
    rospy.loginfo("type_g2 = %s" % type_g2)


