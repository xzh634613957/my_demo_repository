## 6.3 URDF语法详解

URDF 文件是一个标准的 XML 文件，在 ROS 中预定义了一系列的标签用于描述机器人模型，机器人模型可能较为复杂，但是 ROS 的 URDF 中机器人的组成却是较为简单，可以主要简化为两部分:连杆\(link标签\) 与 关节\(joint标签\)，接下来我们就通过案例了解一下 URDF 中的不同标签:

* robot 根标签，类似于 launch文件中的launch标签
* link 连杆标签
* joint 关节标签
* gazebo 集成gazebo需要使用的标签

关于gazebo标签，后期在使用 gazebo 仿真时，才需要使用到，用于配置仿真环境所需参数，比如: 机器人材料属性、gazebo插件等，但是该标签不是机器人模型必须的，只有在仿真时才需设置

---

**另请参考:**

* [https://wiki.ros.org/urdf/XML](https://wiki.ros.org/urdf/XML)

#### 



