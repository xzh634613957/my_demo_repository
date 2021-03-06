## 2.3 参数服务器

参数服务器在ROS中主要用于实现不同节点之间的数据共享。参数服务器相当于是独立于所有节点的一个公共容器，可以将数据存储在该容器中，被不同的节点调用，当然不同的节点也可以往其中存储数据，关于参数服务器的典型应用场景如下:

> 导航实现时，会进行路径规划，比如: 全局路径规划，设计一个从出发点到目标点的大致路径。本地路径规划，会根据当前路况生成时时的行进路径

上述场景中，全局路径规划和本地路径规划时，就会使用到参数服务器：

* 路径规划时，需要参考小车的尺寸，我们可以将这些尺寸信息存储到参数服务器，全局路径规划节点与本地路径规划节点都可以从参数服务器中调用这些参数

参数服务器，一般适用于存在数据共享的一些应用场景。

---

#### **概念**

以共享的方式实现不同节点之间数据交互的通信模式。

#### **作用**

存储一些多节点共享的数据，类似于全局变量。

#### **案例**

实现参数增删改查操作。

---

**另请参考:**

* [http://wiki.ros.org/Parameter%20Server](http://wiki.ros.org/Parameter Server)

* [http://wiki.ros.org/roscpp/Overview/Parameter%20Server](http://wiki.ros.org/roscpp/Overview/Parameter Server)

* [http://wiki.ros.org/rospy/Overview/Parameter%20Server](http://wiki.ros.org/rospy/Overview/Parameter Server)



