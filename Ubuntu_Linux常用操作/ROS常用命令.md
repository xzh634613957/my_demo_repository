## ROS常用命令

### 终端命令

**catkin_make**      <u>编译命令</u>

**roscore**  <u>启动ROS master、参数服务器、日志节点</u>

**rosrun *包名* *节点名***　<u>运行指定的ROS节点</u>

**roslaunch *包名* *launch文件名***　<u>执行某个包下的launch文件</u>

**rqt_graph**　<u>查看不同节点之间的关系</u>

**source ./devel/setup.bash**   <u>修改环境变量</u>

**roscpp rospy std_msgs**    <u>添加依赖</u>

**code . **      <u>在工作空间内启动vscode</u>

catkin_create_pkg  *ROS包名*   <u>创建ROS功能包</u>

rospack list        <u>列出所有功能包</u>

rospack find *包名*    <u>查找某个包是否存在，若存在则返回安装路径</u>

roscd *包名*　　　<u>进入某个功能包</u>

rosls  *包名*　　　<u>列出某个包下的文件</u>

apt search XXX   <u>搜索某个功能包</u>

rosed *包名* *文件名*　<u>修改功能包下的文件名</u>

echo "source ~/工作空间/devel/setup.bash" >> ~/.bashrc   <u>将修改的环境变量添加到 .bashrc文件中，这样就可以在任意终端执行																										ROS命令了</u>



### 命令行工具

- 参考: http://wiki.ros.org/ROS/CommandLineTools

**rosnode** : 操作节点, 用于获取节点信息的命令

```shell
rosnode ping             测试到节点的连接状态
rosnode list                列出活动节点
rosnode info              打印节点信息
rosnode machine     列出指定设备上节点
rosnode kill                 杀死某个节点
rosnode cleanup       清除不可连接的节点
```

**rostopic** : 操作话题, 用于显示有关ROS 话题的调试信息,包括发布者,订阅者,发布频率和ROS消息

```shell
rostopic bw             显示话题使用的带宽
rostopic delay        显示带有 header 的话题延迟
rostopic echo         **打印消息到屏幕**
rostopic echo  话题名称 >> 文件名       **打印消息到指定文件**
rostopic find           根据类型查找话题
rostopic hz              显示话题的发布频率
rostopic info           **显示话题相关信息**
rostopic list             **显示所有活动状态下的话题**
rostopic pub -r 10 话题名称 话题类型      **将数据发布到话题(-r 10 设置发布频率)**
rostopic type          **打印话题使用的消息类型**
```

**rosservice** : 操作服务, 用于列出和查询ROSServices的rosservice命令行工具

```shell
rosservice args      打印服务参数
rosservice call       使用提供的参数调用服务
rosservice find       按照服务类型查找服务
rosservice info       **打印有关服务的信息**
rosservice list         **列出所有活动的服务**
rosservice type      **打印服务类型**
rosservice uri          打印服务的 ROSRPC uri
```

**rosmsg** : 操作msg消息, 用于显示有关 ROS消息类型的信息

```shell
rosmsg show             **显示消息描述**
rosmsg info                **显示消息信息**
rosmsg list                  **列出所有消息**
rosmsg md5               显示 md5 加密后的消息
rosmsg package       显示某个功能包下的所有消息
rosmsg packages     列出包含消息的功能包
```

**rossrv** : 操作srv消息, 用于显示有关ROS服务类型的信息的命令行工具,与 rosmsg 使用语法高度雷同

```shell
rossrv show            **显示服务消息详情**
rossrv info               **显示服务消息相关信息**
rossrv list                 **列出所有服务信息**
rossrv md5              显示 md5 加密后的服务消息
rossrv package      显示某个包下所有服务消息
rossrv packages    显示包含服务消息的所有包
```

**rosparam** : 操作参数, 用于使用YAML编码文件在参数服务器上获取和设置ROS参数

```shell
rosparam set           设置参数
rosparam get           获取参数
rosparam load        从外部文件加载参数
rosparam dump     将参数写出到外部文件
rosparam delete     删除参数
rosparam list            **列出所有参数**
```

**启动键盘控制节点**: 使用键盘控制机器人(通过/cmd_vel话题)

```shell
rosrun teleop_twist_keyboard teleop_twist_keyboard.py _speed:=0.3 _turn:=0.5       speed设置线速度, turn设置角速度(可以不设置)
```



### 常用API(Python)

参考:  https://wiki.ros.org/APIs

**初始化: rospy.init(name,argv,anonymous)**

```
作用: ROS节点初始化
参数: name ---  设置节点名称
			argv=None ---  封装节点调用时传递的参数
			anonymous=False  ---  可以为节点名称生成随机后缀, 解决节点重名的问题
使用: 1) argv使用: 可以按照ROS中指定的语法格式传参, ROS可以解析并加以使	          								用.
			2) anonymous使用: 设置值为True
```

**发布对象: rospy.Publisher(name,data_class,queue_size,latch)**

```
作用: 创建发布者对象
参数: name  ---  话题名称
			data_class  ---  消息类型
			queue_size  ---  等待发送给订阅者的最大消息数量
			latch  ---  该话题发布的最后一条消息将被保存, 并且当后期有订阅者连接时 									会将该消息发送给订阅者
```

**订阅对象: rospy.Subscriber(name,data_class,callback,queue_size)**

**服务对象: rospy.Service(name,service_class,handler)**

**客户端对象: rospy.ServiceProxy(name,service_class)**

**时间:**

* 时刻

  ```python
  # 获取当前时刻
  right_now = rospy.Time.now()
  rospy.loginfo("当前时刻:%.2f",right_now.to_sec())
  rospy.loginfo("当前时刻:%.2f",right_now.to_nsec())
  # 自定义时刻
  some_time1 = rospy.Time(1234.567891011)
  some_time2 = rospy.Time(1234,567891011)
  rospy.loginfo("设置时刻1:%.2f",some_time1.to_sec())
  rospy.loginfo("设置时刻2:%.2f",some_time2.to_sec())
  # 从某个时间值获取时间对象
  some_time3 = rospy.Time.from_sec(543.21) 
  rospy.loginfo("设置时刻3:%.2f",some_time3.to_sec())
  ```

* 持续时间

  ```python
  # 持续时间相关API
  rospy.loginfo("持续时间测试开始.....")
  du = rospy.Duration(3.3)
  rospy.loginfo("du1 持续时间:%.2f",du.to_sec())
  rospy.sleep(du) #休眠函数
  rospy.loginfo("持续时间测试结束.....")
  ```

* 持续时间与时刻运算

  ```python
  rospy.loginfo("时间运算")
  now = rospy.Time.now()
  du1 = rospy.Duration(10)
  du2 = rospy.Duration(20)
  rospy.loginfo("当前时刻:%.2f",now.to_sec())
  before_now = now - du1
  after_now = now + du1
  dd = du1 + du2
  # now = now + now #非法
  rospy.loginfo("之前时刻:%.2f",before_now.to_sec())
  rospy.loginfo("之后时刻:%.2f",after_now.to_sec())
  rospy.loginfo("持续时间相加:%.2f",dd.to_sec())
  ```

* 设置运行频率

  ```python
  # 设置执行频率
  rate = rospy.Rate(0.5)
  while not rospy.is_shutdown():
  		rate.sleep() #休眠
  		rospy.loginfo("+++++++++++++++")
  ```

* 定时器

  ```python
  #定时器设置
  """
  def __init__(self, period, callback, oneshot=False, reset=False):
  Constructor.
  		@param period: 回调函数的时间间隔
  		@type period: rospy.Duration
  		@param callback: 回调函数
  		@type callback: function taking rospy.TimerEvent
  		@param oneshot: 设置为True,就只执行一次,否则循环执行
  		@type oneshot: bool
  		@param reset: if True, timer is reset when rostime moved backward 		                                     [default: False]
  		@type reset: bool
  """
  rospy.Timer(rospy.Duration(1),doMsg)
  # rospy.Timer(rospy.Duration(1),doMsg,True) # 只执行一次
  rospy.spin()
  
  #回调函数
  def doMsg(event):
  		rospy.loginfo("+++++++++++")
  		rospy.loginfo("当前时刻:%s",str(event.current_real))
  ```


**关闭节点: **

* 节点状态判断: is_shutdown()
* 节点关闭: signal_shutdown(renson)
* 节点关闭时执行回调函数: on_shutdown(callback)

**日志函数:**

* 日志等级

  ```
  DEBUG(调试):只在调试时使用,此类消息不会输出到控制台;
  INFO(信息):标准消息,一般用于说明系统内正在执行的操作;
  WARN(警告):提醒一些异常情况,但程序仍然可以执行;
  ERROR(错误):提示错误信息,此类错误会影响程序运行;
  FATAL(严重错误):此类错误将阻止节点继续运行。
  ```

* 函数

  ```python
  rospy.logdebug("hello,debug") #不会输出
  rospy.loginfo("hello,info") #默认白色字体
  rospy.logwarn("hello,warn") #默认黄色字体
  rospy.logerr("hello,error") #默认红色字体
  rospy.logfatal("hello,fatal") #默认红色字体
  ```

**坐标变换:**

```python
ps_out = buffer.transform(ps, "base_link")
 """
	 API: transform(参数1, 参数2)
	 参数1: 被转换的坐标点
	 参数2: 要转换的目标坐标系
	 返回值: 转换后的坐标点
"""
ts = buffer.lookup_transform("son2", "son1", rospy.Time(0))
"""
	API: lookup_transform(参数1, 参数2, 参数3)
    参数1: 目标坐标系
    参数2: 原坐标系
    参数3: 时间关系
    返回值: 原坐标系与目标坐标系的关系
"""
```



### VSCode

Ctrl + Shift + B    <u>调用编译(catkin_make:build)</u>

​			使用 Ctrl + Shift + B 默认快捷编译ROS，需要修改.vscode/tasks.json文件：

```c++
{
// 有关 tasks.json 格式的文档，请参见
    // https://go.microsoft.com/fwlink/?LinkId=733558
    "version": "2.0.0",
    "tasks": [
        {
            "label": "catkin_make:debug", //代表提示的描述性信息
            "type": "shell",  //可以选择shell或者process,如果是shell代码是在shell里面运行一个命令，如果是process代表作为一个进程来运行
            "command": "catkin_make",//这个是我们需要运行的命令
            "args": [],//如果需要在命令后面加一些后缀，可以写在这里，比如-DCATKIN_WHITELIST_PACKAGES=“pac1;pac2”
            "group": {"kind":"build","isDefault":true},
            "presentation": {
                "reveal": "always"//可选always或者silence，代表是否输出信息
            },
            "problemMatcher": "$msCompile"
        }
    ]
}                              
```

设置解释器以及Python2中文编码: 

```python
#! /usr/bin/env python
#coding:utf-8
```

设置C++输出中文:

```c++
setlocale(LC_CTYPE, "zh_CN.utf8");
setlocale(LC_ALL, "");
```

Ctrl + K, Ctrl + C   <u>多行注释</u>

Ctrl + K, Ctrl + U   <u>取消多行注释</u>

Ctrl + /      <u>单行注释</u>



### ROS数据类型

![](/home/xiongzh/文档/Ubuntu_Linux常用操作/ROS常用命令.assets/ROS数据类型.png)



### launch 文件标签

* **node:** 指定ROS节点(roslaunch命令不能保证按照node的声明顺序来启动节点)
* **include:** 复用已经存在的launch文件, 减少代码重复
* **remap:** 用于话题重命名
* **param:** 用于在参数服务器上设置参数
* **rosparam:** 用于从yaml文件导入参数, 或将参数导出到yaml文件
* **group:** 对节点进行分组, 可以启动多个相同的节点
* **arg:** 用于动态传参, 类似于函数的参数



### 重命名

* **节点重命名**

   * rosrun设置命名空间与重映射

     ```c++
     rosrun 包名 节点名 __ns:=新名称      // 设置命名空间
     rosrun 包名 节点名 __name:=新名称  //重映射
     rosrun 包名 节点名ns:=新名称 name:=新名称  // 设置命名空间与重映射叠加
     ```

   * launch文件设置命名空间和重映射

     ```xml
     <!-- 重映射 -->
     <node pkg="包名" type="节点类型" name="新名称" />  
     <!-- 设置命名空间 -->
     <node pkg="包名" type="节点类型" name="节点名称" ns="新名称" /> 
     <!-- 设置命名空间与重映射叠加当初速度 -->
     <node pkg="包名" type="节点类型" name="新名称" ns="新名称" /> 
     ```

   * 编码设置重映射

     ```python
     rospy.init_node("节点名称", anonymous=True)  # 给节点名称后面增加随机后缀
     ```

* **话题重命名**

    * rosrun设置话题重映射

      ~~~python
      rosrun 包名 节点名 话题名:=新话题名
      ~~~

   * launch设置话题重映射

     ```xml
     <node pkg="包名" type="节点类型" name="节点名称">
         	<remap from="原话题" to="新话题" />
     </node>
     ```

   * 编码设置话题名称(Python)

     ~~~Python
     pub = rospy.Publisher("/话题名称", String, queue_size=10)  # 设置全局话题
     pub = rospy.Publisher("话题名称", String, queue_size=10)  # 设置相对话题
     pub = rospy.Publisher("~话题名称", String, queue_size=10)  # 设置私有话题
     ~~~

* **参数重命名**

   * rosrun设置参数

      ```
      rosrun 包名 节点名 _参数名:=参数值  // 默认为私有参数
      ```

   * launch文件设置参数

      ```xml
      <launch>
              <!-- 在node标签外设置全局参数 -->
              <para name="参数名" value="参数值" />
              <node pkg="包名" type="节点类型" name="节点名称" ns="命名空间">
                  <!-- 在node标签外设置私有参数 -->
                  <para name="参数名" value="参数值" />
              </node>
      </launch>
          
      ```

   * 编码设置参数(Python API)

      ```python
      rospy.set_param("/参数名", 参数值)  # 全局参数, 与命名空间和节点名称无关
      rospy.set_param("参数名", 参数值)  # 相对参数, 参考命名空间
      rospy.set_param("~参数名", 参数值)  # 私有参数, 参考命名空间与节点名称
      ```




### ROS常用组件

* **tf2_tools**

  * **坐标系关系查看**

    在机器人系统中，涉及的坐标系有多个，为了方便查看，ros 提供了专门的工具，可以用于生成显示坐标系关系的 pdf 文件，该文件包含树形结构的坐标系图谱。启动坐标系广播程序之后，运行如下命令后会在工作空间目录生成PDF文件.

    ```shell
    rosrun tf2_tools view_frames.py
    ```

* **rosbag**

  * 参考: http://wiki.ros.org/rosbag

  * 用于录制和回放 ROS 话题的一个工具集, 实现了数据的复用，方便调试、测试.

  * rosbag本质也是ros的节点，当录制时，rosbag是一个订阅节点，可以订阅话题消息并将订阅到的数据写入磁盘文件；当重放时，rosbag是一个发布节点，可以读取磁盘文件，发布文件中的话题消息.

  * 常用命令行

    ```shell
    rosbag record -a -o 文件路径/文件名.bag  # 开始录制(-a: 录制所有话题; -o: 设置输出路径)
    rosbag info 文件路径/文件名.bag  # 查看录制的文件
    rosbag play 文件路径/文件名.bag  # 回放录制的文件
    ```


* **rqt工具箱**

  * 参考: http://wiki.ros.org/rqt

  * 可以方便的实现 ROS 可视化调试，并且在同一窗口中打开多个部件，提高开发效率，优化用户体验

  * 启动: `rqt`

  * 常用插件

    ```shell
    rqt_graph  # 可视化显示计算图(显示节点, 话题等信息)(Plugins/Introspection/Node Graph)
    rqt_console  # 用于显示和过滤日志的图形化插件 (Plugins/Logging/Console)
    rqt_plot  # 图形绘制插件，可以以 2D 绘图的方式绘制发布在 topic 上的数据(Plugins/Visualization/Plot)
    rqt_bag  # 录制和重放 bag 文件的图形化插件(Plugins/Logging/Bag)
    ```

* **URDF**
  * 参考: https://wiki.ros.org/urdf
  
  * ```shell
    check_urdf  # 检查复杂的 urdf 文件是否存在语法问题
    urdf_to_graphiz   # 查看 urdf 模型结构，显示不同 link 的层级关系
    ```
  
  * 
* **rviz**
  
  * 参考: http://wiki.ros.org/rviz
  
* **Gazebo**
  
  * 参考: http://gazebosim.org/tutorials?tut=ros_overview

* **Xacro**

  * 将xacro文件解析为urdf文件:

    ```shell
    rosrun xacro xacro 文件名.xacro > 文件名.urdf
    ```



### ROS报错

* ROS 使用move_base导航包时出现错误

  ```shell
  [ERROR] [1640758370.147889281, 1191.636000000]: Extrapolation Error: Lookup would require extrapolation into the future.  Requested time 1191.635000000 but the latest data is at time 1191.595000000, when looking up transform from frame [odom] to frame [map]
  ```

  * 参考: https://blog.csdn.net/CMLHYD/article/details/90294265?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=1
  * 这种情况是 amcl 中的 transform_tolerance 的值设置太小 一般改为 1 就不会出现问题。这个参数是关于坐标变换时间容忍度，大概意思是你的系统能使用多长时间之前的坐标变化。或者TF变换在多久内有效。







