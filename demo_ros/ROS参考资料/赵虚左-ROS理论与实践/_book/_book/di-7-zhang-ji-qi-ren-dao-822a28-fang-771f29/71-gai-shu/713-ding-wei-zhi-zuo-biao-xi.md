### 7.1.3导航条件说明

导航实现，在硬件和软件方面是由一定要求的，需要提前准备。

#### 1.硬件

虽然导航功能包集被设计成尽可能的通用，在使用时仍然有三个主要的硬件限制：

1. 它是为差速驱动的轮式机器人设计的。它假设底盘受到理想的运动命令的控制并可实现预期的结果，命令的格式为：x速度分量，y速度分量，角速度\(theta\)分量。

2. 它需要在底盘上安装一个单线激光雷达。这个激光雷达用于构建地图和定位。

3. 导航功能包集是为正方形的机器人开发的，所以方形或圆形的机器人将是性能最好的。 它也可以工作在任意形状和大小的机器人上，但是较大的机器人将很难通过狭窄的空间。

#### 2.软件

导航功能实现之前，需要搭建一些软件环境:

1. 毋庸置疑的，必须先要安装 ROS

2. 当前导航基于仿真环境，先保证上一章的机器人系统仿真可以正常执行

   在仿真环境下，机器人可以正常接收 /cmd\_vel 消息，并发布里程计消息，传感器消息发布也正常，也即导航模块中的运动控制和环境感知实现完毕

后续导航实现中，我们主要关注于: 使用 SLAM 绘制地图、地图服务、自身定位与路径规划。

---



