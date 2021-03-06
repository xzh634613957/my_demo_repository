## 2.2 服务通信

服务通信也是ROS中一种极其常用的通信模式，服务通信是基于**请求响应**模式的，是一种应答机制。也即: 一个节点A向另一个节点B发送请求，B接收处理请求并产生响应结果返回给A。比如如下场景:

> 机器人巡逻过程中，控制系统分析传感器数据发现可疑物体或人... 此时需要拍摄照片并留存。

在上述场景中，就使用到了服务通信。

* 一个节点需要向相机节点发送拍照请求，相机节点处理请求，并返回处理结果

与上述应用类似的，服务通信更适用于对时时性有要求、具有一定逻辑处理的应用场景。

---

#### **概念**

以请求响应的方式实现不同节点之间数据交互的通信模式。

#### **作用**

用于偶然的、对时时性有要求、有一定逻辑处理需求的数据传输场景。

#### 案例

实现两个数字的求和，客户端节点，运行会向服务器发送两个数字，服务器端节点接收两个数字求和并将结果响应回客户端。

![](/assets/02.03_请求响应.gif)

---

**另请参考:**

* [http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)

* [http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29)

* [http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)



