#! /usr/bin/env python
# coding: utf-8

"""
    动态坐标变换
    需求描述:
        启动 turtlesim_node,该节点中窗体有一个世界坐标系(左下角为坐标系原点),乌龟是另一个坐标系,键
        盘控制乌龟运动,将两个坐标系的相对位置动态发布。
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
        3. 订阅话题 /turtle1/pose 话题
        4. 回调函数处理消息数据()
            4.1 创建发布者对象
            4.2 创建用于表示坐标系相对姿态的消息对象
            4.3 发布者发布消息
        5. spin()
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
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
# import tf.transformations
import tf_conversions


# 4. 回调函数处理消息数据()
def doPose(pose):

    # 4.1 创建发布者对象(需要导入tf2_ros)
    pub = tf2_ros.TransformBroadcaster()
    # 4.2 创建用于表示坐标系相对姿态的消息对象(需要导入TransformStamped)
    tfs = TransformStamped()
    tfs.header.frame_id = "world"
    tfs.header.stamp = rospy.Time.now()
    tfs.child_frame_id = "turtle1"
    tfs.transform.translation.x = pose.x
    tfs.transform.translation.y = pose.y
    tfs.transform.translation.z = 0.0
    # (需要导入tf.transformations)
    qtn = tf_conversions.transformations.quaternion_from_euler(0, 0, pose.theta)
    tfs.transform.rotation.x = qtn[0]
    tfs.transform.rotation.y = qtn[1]
    tfs.transform.rotation.z = qtn[2]
    tfs.transform.rotation.w = qtn[3]
    # 4.3 发布者发布消息
    pub.sendTransform(tfs)


if __name__ == "__main__":
        
        # 2. 初始化节点(需要导入rospy)
        rospy.init_node("dynamic_tf_pub")
        
        # 3. 订阅话题 /turtle1/pose 话题(需要导入Pose)
        sub = rospy.Subscriber("/turtle1/pose", Pose, doPose)

        # 5. spin()
        rospy.spin()
        
