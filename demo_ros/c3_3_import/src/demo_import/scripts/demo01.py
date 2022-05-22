#! /usr/bin/env python3


"""
    通过可执行文件调用工具函数中的参数
    当导入其他python模块出现错误: No module named "tools" 时,可用以下办法解决
"""

import rospy
# import tools //执行这段语句时可能会报错: No module named "tools"
import os
import sys

path = os.path.abspath(".")
sys.path.insert(0, path + "/src/demo_import/scripts")

import tools

if __name__ == "__main__":
    rospy.init_node("import_tools")
    rospy.loginfo("工具包的调用 num = %d" % tools.num)