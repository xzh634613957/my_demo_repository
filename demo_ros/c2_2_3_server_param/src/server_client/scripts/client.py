#! /usr/bin/env python
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

    优化: 加入数据的动态获取
"""

import rospy
from server_client.srv import AddInts,AddIntsRequest,AddIntsResponse
# from server_client.srv import * --- 全部导入
import sys


if __name__ == "__main__":
    
    # 判断用户输入的参数个数
    if len(sys.argv) != 3:
        rospy.logerr("请输入正确的参数!")
        sys.exit(1)

    rospy.init_node("Client")

    client = rospy.ServiceProxy("topic",AddInts)
    rospy.loginfo("客户端已启动, 正在等待服务器响应...")
    
    require = AddIntsRequest()
    require.num1 = int(sys.argv[1])
    require.num2 = int(sys.argv[2])

    # 等待服务器响应
    client.wait_for_service()
    # rospy.wait_for_service("topic")

    respose = client.call(require)

    rospy.loginfo("响应的结果为: %d" % respose.sum)


