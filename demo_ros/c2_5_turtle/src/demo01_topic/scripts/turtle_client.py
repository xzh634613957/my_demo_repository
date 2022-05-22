#! /usr/bin/env python
# coding: utf-8

"""
    客户端实现: 向服务端发送增加小乌龟的需求,并接收服务端响应
        服务话题: /spawn (rosservice list)
        服务消息: turtlesim/Spawn (rosservice info /spawn)
        消息类型: (rossrv info turtlesim/Spawn)
                float32 x
                float32 y
                float32 theta
                string name
                ---
                string name
"""

import rospy
from turtlesim.srv import *



if __name__ == "__main__":
    rospy.init_node("turtle_client")
    client = rospy.ServiceProxy("/spawn",Spawn)

    client.wait_for_service()

    require = SpawnRequest()
    require.x = 2.0
    require.y = 4.0
    require.theta = 2.0
    require.name = "turtle2"

    try:
        response = client.call(require)
        # 处理响应
        rospy.loginfo("%s乌龟创建成功!" % response.name)
    except Exception as identifier:
        rospy.loginfo("服务调用失败!")

