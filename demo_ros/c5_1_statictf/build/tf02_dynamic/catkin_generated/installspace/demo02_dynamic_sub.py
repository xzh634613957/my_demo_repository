#!/usr/bin/env python2
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
"""

# 1. 导包
import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs


if __name__ == "__main__":

    # 2. 初始化ROS节点(需要导入rospy)
    rospy.init_node("dynamic_tf_sub")

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
        # 注意这里, 动态坐标变换的时间戳与静态坐标变化的时间戳不一样, 这里不能使用 rospy.Time.now(), 否则会报错
        ps.header.stamp = rospy.Time()  
        ps.header.frame_id = "turtle1"
        ps.point.x = 2.0
        ps.point.y = 3.0
        ps.point.z = 5.0

    # 5.调用订阅对象的 API 将 radar 坐标系中的点坐标转换成相对于 base_link 坐标系的坐标
        # 当还没监听到数据时, transform就开始转换了, 这时会报错 base_link 找不到, 因此要处理异常
        # 用 try 捕获异常后, 当没监听数据时会提示警告信息, 而不会报错
        try:
            ps_out = buffer.transform(ps, "world")
            """
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

    # 6.spin
        rate.sleep()


