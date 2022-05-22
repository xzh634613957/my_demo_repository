#! /usr/bin/env python
# coding: utf-8

"""
    调用 Server-Client 在乌龟GUI上指定位置生成一只乌龟
    流程:
        1.导包
        2.初始化ROS节点
        3.创建服务客户端对象
        4.等待服务启动
        5.创建请求数据
        6.发送请求并处理响应
"""

# 1.导包
import rospy
from turtlesim.srv import *



if __name__ == "__main__":
   
    # 2.初始化ROS节点
    rospy.init_node("new_turtle")

    # 3.创建服务客户端对象
    client = rospy.ServiceProxy("/spawn", Spawn)
    """
        参数1: 服务名称(使用 rosservice list 查看)
        参数2: 服务类型(使用 rosservice type /spawn(或 rosservice info /spawn) 查看)
    """
    rospy.loginfo("客户端已启动, 正在等待服务端响应...")

    # 4.等待服务启动
    client.wait_for_service()

    # 5.创建请求数据
    req = SpawnRequest()
    """
        使用 rossrv info turtlesim/Spawn 查看服务端-客户端的消息信息
            请求信息(客户端发送, 服务端接收):
                float32 x
                float32 y
                float32 theta
                string name
                ---
            响应信息(服务端发送, 客户端接收):
                string name
    """
    req.x = 4.5
    req.y = 2.0
    req.theta = 0
    req.name = "turtle2"

    # 6.发送请求并处理响应
    try:
        respose = client.call(req)
        rospy.loginfo("%s创建成功" % respose.name)

    except Exception as e:
        rospy.loginfo("服务调用失败: %s" % e)
