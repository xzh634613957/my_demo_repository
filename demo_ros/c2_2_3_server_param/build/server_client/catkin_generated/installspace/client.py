#!/usr/bin/env python2
#coding:utf-8

"""
    需求: 编写两个节点实现服务通信.
        1. 客户端节点提交两个整数到服务端 
        2. 服务端解析客户所提交的数据
        3. 服务端将两个整数相加后返回结果给客户端
        4. 客户端解析服务端返回的数据
    
    客户端实现:
        1. 导包
        2. 初始化ROS节点
        3. 创建客户端对象
        4. 组织请求数据并发送请求
        5. 接受并处理服务端相应
"""

import rospy
from server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
# from server_client.srv import * --- 全部导入


if __name__ == "__main__":
    rospy.init_node("Client")
    client = rospy.ServiceProxy("topic",AddInts)
    require = AddIntsRequest()
    require.num1 = 10
    require.num2 = 20
    respose = client.call(require)
    rospy.loginfo("相应的结果为: %d" % respose.sum)


