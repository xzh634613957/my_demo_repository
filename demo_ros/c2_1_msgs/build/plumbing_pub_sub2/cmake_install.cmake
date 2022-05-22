# Install script for directory: /home/xiongzh/demo_ros/demo3_2/src/plumbing_pub_sub2

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/xiongzh/demo_ros/demo3_2/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/plumbing_pub_sub2/msg" TYPE FILE FILES "/home/xiongzh/demo_ros/demo3_2/src/plumbing_pub_sub2/msg/Person.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/plumbing_pub_sub2/cmake" TYPE FILE FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/plumbing_pub_sub2-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/xiongzh/demo_ros/demo3_2/devel/include/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/xiongzh/demo_ros/demo3_2/devel/share/roseus/ros/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/xiongzh/demo_ros/demo3_2/devel/share/common-lisp/ros/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/xiongzh/demo_ros/demo3_2/devel/share/gennodejs/ros/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/xiongzh/demo_ros/demo3_2/devel/lib/python2.7/dist-packages/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/xiongzh/demo_ros/demo3_2/devel/lib/python2.7/dist-packages/plumbing_pub_sub2")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/plumbing_pub_sub2.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/plumbing_pub_sub2/cmake" TYPE FILE FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/plumbing_pub_sub2-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/plumbing_pub_sub2/cmake" TYPE FILE FILES
    "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/plumbing_pub_sub2Config.cmake"
    "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/plumbing_pub_sub2Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/plumbing_pub_sub2" TYPE FILE FILES "/home/xiongzh/demo_ros/demo3_2/src/plumbing_pub_sub2/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/plumbing_pub_sub2" TYPE PROGRAM FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/demo02_pub_p.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/plumbing_pub_sub2" TYPE PROGRAM FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/demo02_sub_p.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/plumbing_pub_sub2" TYPE PROGRAM FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/demo03_pub.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/plumbing_pub_sub2" TYPE PROGRAM FILES "/home/xiongzh/demo_ros/demo3_2/build/plumbing_pub_sub2/catkin_generated/installspace/demo03_sub.py")
endif()

