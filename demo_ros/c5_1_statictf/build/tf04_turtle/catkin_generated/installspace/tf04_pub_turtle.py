#!/usr/bin/env python2
# coding: utf-8

"""
    该文件实现:需要订阅 turtle1 和 turtle2 的 pose，然后广播相对 world 的坐标系信息
"""
"""
    实现分析:
        1. 乌龟本身不但可以看做为一个坐标系, 它也是世界坐标系中的一个坐标点
        2. 订阅 turtle1/pose, 可以获得乌龟在世界坐标系的x, y, theta, linear_velocity, angular_velocity
            2.1 使用 rostopic list 可以查到乌龟发布位姿的话题为:  /turtle1/pose
            2.2 使用 rostopic info /turtle1/pose 可以查到话题使用的消息类型为: turtlesim/Pose
            2.3 使用 rosmsg info turtlesim/Pose 可以查到消息类型传递的具体数据类型为:
                float32 x
                float32 y
                float32 theta
                float32 linear_velocity
                float32 angular_velocity
        3. 将 pose 信息转换为坐标系的相对信息并发布
        4. 相当于这个节点又当订阅者(订阅乌龟位姿话题), 又当发布者(发布乌龟坐标系相对于世界坐标系的位置)
            也就是在用回调函数处理订阅到的数据时, 将数据转换为坐标系相对关系后发布出去
        5. 总的来说, 就是先订阅位姿信息, 再转换为世界坐标, 最后再发布坐标信息
"""
"""
    实现流程:
        1. 导包
        2. 初始化节点
        3. 解析传入的动态参数(args)
        4. 创建订阅对象订阅 /turtle1/pose 话题 或 /turtle2/pose 话题
        5. 回调函数处理消息数据()
            4.1 创建发布者对象
            4.2 创建用于表示坐标系相对姿态的消息对象
            4.3 发布者发布消息
        6. spin()
"""
"""
    TransformStamped (msg文件) ---  用于表示坐标系的相对姿态(发布方的消息格式)
        std_msgs/Header header #头信息
            uint32 seq #|-- 序列号
            time stamp #|-- 时间戳
            string frame_id #|-- 坐标 ID
        string child_frame_id #子坐标系的 id
        geometry_msgs/Transform transform #坐标信息
            geometry_msgs/Vector3 translation #偏移量
                float64 x #|-- X 方向的偏移量
                float64 y #|-- Y 方向的偏移量
                float64 z #|-- Z 方向上的偏移量
            geometry_msgs/Quaternion rotation #四元数
                float64 x
                float64 y
                float64 z
                float64 w
"""


# 1. 导包
import rospy
import sys
import tf2_ros
from turtlesim.msg import Pose
from geometry_msgs.msg import TransformStamped
import tf_conversions

# 用全局变量接收传入的动态参数args(因为这个变量既要在doPose中使用,也要在主函数中使用)
turtle_name = ""


# 5. 回调函数处理消息数据()
def doPose(pose):

    # 5.1 创建发布者对象
    pub = tf2_ros.TransformBroadcaster()

    # 5.2 创建用于表示坐标系相对姿态的消息对象
    # 5.2.1 头信息
    tfs = TransformStamped()
    tfs.header.frame_id = "world"
    tfs.header.stamp = rospy.Time.now()

    # 5.2.2 子坐标系
    # 动态参数需要修改的第二个地方: 子坐标系的名称
    tfs.child_frame_id = turtle_name

    # 5.2.3 坐标信息
    tfs.transform.translation.x = pose.x
    tfs.transform.translation.y = pose.y
    tfs.transform.translation.z = 0.0

    qtn = tf_conversions.transformations.quaternion_from_euler(0, 0, pose.theta)
    tfs.transform.rotation.x = qtn[0]
    tfs.transform.rotation.y = qtn[1]
    tfs.transform.rotation.z = qtn[2]
    tfs.transform.rotation.w = qtn[3]

    # 5.3 发布者发布消息
    pub.sendTransform(tfs)


if __name__ == "__main__":
    # 2. 初始化节点
    rospy.init_node("dynamic_tf_pub")

    # 3. 解析传入的参数(args)(需要导入sys)
        # 3.1 判断传入的参数个数
            # 使用launch文件传入的args参数只有一个, 但是解释器解析的参数不只这一个, 而是包括了以下几个参数:
            #     a. 文件路径
            #     b. 传入的参数(这个参数是我们需要用的)
            #     c. 节点名称
            #     d. 日志文件路径
    if len(sys.argv) != 4:
        rospy.loginfo("您输入的参数不正确, 请重新输入!")
        sys.exit(1)
    else:
        turtle_name = sys.argv[1]  # 对应解释文档里的 b.传入的参数
    
    rospy.loginfo("----------------------乌龟: %s" % turtle_name)

    # 4. 创建订阅对象订阅 /turtle1/pose 话题 或 /turtle2/pose 话题
    # 动态参数需要修改的第一个地方: 订阅的话题名称
    sub = rospy.Subscriber(turtle_name + "/pose", Pose, doPose)

    # 6. spin()
    rospy.spin()
