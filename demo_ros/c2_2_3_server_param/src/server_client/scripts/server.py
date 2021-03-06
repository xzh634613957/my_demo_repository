#! /usr/bin/env python
#coding:utf-8

"""
    需求: 编写两个节点实现服务通信.
        1. 客户端节点提交两个整数到服务端 
        2. 服务端解析客户所提交的数据
        3. 服务端将两个整数相加后返回结果给客户端
        4. 客户端解析服务端返回的数据
    
    服务端实现:
        1. 导包
        2. 初始化ROS节点
        3. 创建服务端对象
        4. 处理客户端请求并产生响应(利用回调函数)
        5. 使用 spin() 函数调用回调函数
"""

import rospy
from server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
# from server_client.srv import *

def doReq(require):
    """
        作用: 处理客户端请求并产生响应
        参数: 封装了的请求对象
        返回值: 封装了的响应对象
    """
    sum = require.num1 + require.num2

    rospy.loginfo("服务器响应的结果: %d" % sum)

    respose = AddIntsResponse()
    respose.sum = sum
    return respose


if __name__ == "__main__":

    rospy.init_node("Server")
    
    server = rospy.Service("topic",AddInts,doReq)
    rospy.loginfo("服务端已启动")
    
    rospy.spin()