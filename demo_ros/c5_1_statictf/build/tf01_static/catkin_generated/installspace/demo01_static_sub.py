#!/usr/bin/env python2
# coding: utf-8

"""
    订阅方实现: 订阅坐标系变换信息,生成一个相对于子级坐标系的坐标点数据,转换成父级坐标系中的坐标点
    即: 将要转换的坐标点传给发布方, 然后接受被转换的坐标点
    实现流程:
        1.导包
        2.初始化 ROS 节点
        3.创建 TF 订阅对象
        4.创建一个 radar 坐标系中的坐标点
        5.调用订阅对象的 API(transform) 将 4 中的点坐标转换成相对于 world 的坐标
        6.spin
"""
"""
    geometry_msgs/PointStamped(msg文件)(订阅方的消息格式)
    std_msgs/Header header #头
        uint32 seq #|-- 序号
        time stamp #|-- 时间戳
        string frame_id #|-- 所属坐标系的id
    geometry_msgs/Point point #点坐标
        float64 x  #|-- x y z 坐标
        float64 y
        float64 z
"""

# 1. 导包
import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs


if __name__ == "__main__":

    # 2. 初始化ROS节点(需要导入rospy)
    rospy.init_node("static_tf_sub")

    # 3. 创建TF订阅对象(需要导入tf2_ros)
    # 注意: 订阅对象订阅到的数据在tf2中还需要缓存
    # 3.1 创建缓存对象
    buffer = tf2_ros.Buffer()
    # 3.2 创建订阅对象(将缓存传入)(开始监听发布者发布的坐标关系数据)
    sub = tf2_ros.TransformListener(buffer)

    # 循环发布消息, 实时传入障碍物的坐标点
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

    # 4.创建一个 radar 坐标系中的坐标点(障碍物在雷达中的坐标点)(需要导入tf2_geometry_msgs)
        ps = tf2_geometry_msgs.PointStamped()
        ps.header.stamp = rospy.Time.now()
        ps.header.frame_id = "radar"
        ps.point.x = 2.0
        ps.point.y = 3.0
        ps.point.z = 5.0

    # 5.调用订阅对象的 API 将 radar 坐标系中的点坐标转换成相对于 base_link 坐标系的坐标
        # 当还没监听到数据时, transform就开始转换了, 这时会报错 base_link 找不到, 因此要处理异常
        # 用 try 捕获异常后, 当没监听数据时会提示警告信息, 而不会报错
        try:
            ps_out = buffer.transform(ps, "base_link")
            """
                API: transform(参数1, 参数2)
                参数1: 被转换的坐标点
                参数2: 要转换的目标坐标系
                返回值: 转换后的坐标点
            """
            rospy.loginfo("转换结果: x=%.2f, y=%.2f, z=%.2f", 
                            ps_out.point.x,   
                            ps_out.point.y, 
                            ps_out.point.z)
        except Exception as e:
            rospy.logwarn("错误提示:%s", e)

        rate.sleep()

    # 6.spin


