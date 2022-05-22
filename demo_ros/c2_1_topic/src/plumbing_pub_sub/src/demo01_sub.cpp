#include "ros/ros.h"
#include "std_msgs/String.h"  //1.包含头文件

/*
    订阅方实现:
    1.包含头文件
    2.初始化ROS节点
    3.创建节点句柄
    4.创建订阅者对象
    5.处理订阅到的数据
    6.用span()函数调用回调函数(doMsg)
*/

int main(int argc, char  *argv[])
{
    
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"listener");  //2.初始化ROS节点
    ros::NodeHandle nh;  //3.创建节点句柄
    void doMsg(const std_msgs::String::ConstPtr& msg_p);
    ros::Subscriber sub = nh.subscribe<std_msgs::String>("chatter",10,doMsg);  //4.创建订阅者对象
    ros::spin();  //6.用span()函数调用回调函数(doMsg)

    return 0;
}

void doMsg(const std_msgs::String::ConstPtr& msg_p)  //5.处理订阅到的数据
{
    ROS_INFO("listener订阅的消息为:%s",msg_p->data.c_str());
}