## 8.6 机器人平台设计之底盘实现\(下\)

上一节中，底盘的程序设计是自实现的，其实在ros中还提供了一个已经封装了的串口通信模块: ros\_arduino\_bridge，通过该模块可以更为快捷、方便的实现自己的机器人平台。本节介绍的主要内容如下:

* ros\_arduino\_bridge 的架构

* Arduino端程序修改

* ROS端程序配置

注意:8.5中已有说明，官方提供的案例所需硬件国内不易购买，还需要适配硬件并添加相应的驱动，而关于硬件选择，直接基于8.5已有实现即可。

