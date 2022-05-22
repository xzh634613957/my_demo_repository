#! /usr/bin/env python
# coding: utf-8

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
# import tf
# import tf_conversions
import tf.transformations

"""
    重要:
        当坐标系之间的相对位置是固定时, 可以不用专门写这个发布者节点, 而是用 ROS 系统已经封装好了的
        专门的节点, 直接在命令行输入:
        rosrun tf2_ros static_transform_publisher x偏移量 y偏移量 z偏移量 z偏航角 y俯仰角 z滚转角 父级坐标系 子级坐标系
        比如:
        rosrun tf2_ros static_transform_publisher 0.2 0.2 0.5 0 0 0 /baselink /laser
"""

"""
    静态坐标变换发布方实现: 发布两个坐标系的相对关系(车辆底盘 --- base_link 和 雷达 ---radar)
    流程:
        1. 导包
        2. 初始化节点
        3. 创建发布者对象
        4. 组织发布消息的逻辑
        5. 发布数据
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



if __name__ == "__main__":

    # 2. 初始化节点(需要导入rospy)
    rospy.init_node("static_tf_pub")

    # 3. 创建发布者对象(需要导入tf2_ros)
    pub = tf2_ros.StaticTransformBroadcaster()

    # 4. 组织发布的消息(需要导入TransformStamped)
    # 4.1 创建消息对象
    ts = TransformStamped()
    # 4.2 按照TransformStamped消息的格式来组织消息
    # header --- 头部信息
    ts.header.stamp = rospy.Time.now()
    ts.header.frame_id = "base_link" # 参考坐标系的名称(底盘坐标系)
    # child_frame --- 子坐标系
    ts.child_frame_id = "radar" # 子坐标系的名称(激光雷达坐标系)
    # Transform --- 坐标系相对信息
    # translation --- 位移偏移量
    ts.transform.translation.x = 0.2
    ts.transform.translation.y = 0.0
    ts.transform.translation.z = 0.5
    # rotaion --- 旋转偏移量 (先从欧拉角转换成四元数, 在设置四元数)(需要导入tf和tf.transformations)
    qtn = tf.transformations.quaternion_from_euler(0,0,0)
    # 设置四元数(qtn是一个列表)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]

    # 5. 用发布者发布数据
    pub.sendTransform(ts)
    rospy.loginfo("已发布数据")

    # 6. spin()
    rospy.spin()
    