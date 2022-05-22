#include "ros/ros.h"
#include "std_msgs/String.h" //1.包含头文件(发布者发布的文本信息需要用到该头文件)
#include <sstream> //实现拼接字符和数字

/*
    消息发布方的要求:
    以1Hz的频率循环发布文本信息: Hello World 后缀数字编号    
      
    发布者实现的步骤：
    1.包含头文件
    2.初始化ROS节点
    3.创建(实例化)节点句柄
    4.创建(实例化)发布者对象
    5.编写发布者逻辑并发布
*/


int main(int argc, char  *argv[])
{
    setlocale(LC_ALL,""); //设置中文格式的日志输出
    
    ros::init(argc,argv,"talker"); //2.初始化ROS节点

    ros::NodeHandle nh; //3.实例化节点句柄对象

    ros::Publisher pub = nh.advertise<std_msgs::String>("chatter",10); //实例化发布者对象

    std_msgs::String msg; //5.1 实例化发布的消息

    ros::Rate r(1); //以1Hz的频率发布消息

    int count = 0; //设置编号

    //5.2 编写循环,循环发布数据
    while(ros::ok()) //如果节点一直存在,则一直循环
    {

        msg.data = "Hello World";

        std::stringstream ss; //实例化对象

        ss << msg << count; //拼接字符和数字

        msg.data = ss.str(); //将拼接好的对象属性传给消息对象的属性

        pub.publish(msg); //发布消息

        ROS_INFO("发送的消息是:%s",ss.str().c_str());

        count++;

        r.sleep(); //休眠时间=1/10Hz=0.1s
    }

    return 0;
}
