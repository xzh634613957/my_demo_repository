## Autoware_LGSVL_Carla常用组件及命令

### 1. Autoware

#### 1.1 **常用终端命令**

- **启动autoware**

  ```shell
  cd autoware.ai/
  source install/setup.bash
  roslaunch runtime_manager runtime_manager.launch
  roslaunch naive_motion_predict predict_obstacle_points.launch
  ```

- **编译安装包**

  ```shell
  # 编译所有包
  AUTOWARE_COMPILE_WITH_CUDA=1 colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
  # 单独编译一个包
  AUTOWARE_COMPILE_WITH_CUDA=1 colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release --packages-select waypoint_planner

#### 1.2 常用话题、节点

- **topic**

  ```shell
  /points_raw  # 激光雷达发布的点云数据（发布者：激光雷达）
  /image_raw  # 相机发布的图像数据
  ```
  
  


#### 1.3 **常用组件**

- **坐标系**

  - 世界坐标系：world

  - 地图坐标系：map

  - 车辆坐标系：base_link

  - 传感器坐标系：velodyne

    ![img](https://img2018.cnblogs.com/blog/1023160/201907/1023160-20190706104258109-1114483258.png)

  - 从**world到map**的坐标系转换与从**base_link到velodyne**的坐标系转换是固定的，用ROS的**TF**即可

    - **world_to_map**: **[Map]**页面，**[TF]**选项。默认文件路径：`/home/xiongzh/autoware.ai/src/autoware/documentation/autoware_quickstart_examples/launch/tf_local.launch`

      ```xml
      <launch>
        <node pkg="tf"
          type="static_transform_publisher"
          name="world_to_map"
           <!--从world坐标系转换到/map坐标系的x,y,z,roll,pitch,yaw转换，频率为10Hz -->
          args="0 0 0 0 0 0 /world /map 10"
          />
      </launch>
      ```

    - **base_link_to_velodyne**: **[Setup]**页面，**[Localizer]**选项，选择**[Velodyne]**，在**[Baselink to Localizer]** 中设置好各个参数之后点击 **[TF]** 按钮，其中x、y、z、yaw、pitch、roll表示真车雷达中心点与车身后轴中心点的相对位置关系（右手坐标系，真车后车轴为原点），此时可以点击**[Vehicle Model]**，如果[Vehicle Model]为空，那么会加载一个默认模型

  - 从**map到base_link**的映射就需要scan-to-map的算法，autoware在建图采用的是**ndt matching**

    - **map_to_base_link**: 在 **[Computing]** 菜单栏中找到 **[lidar_localizer]**下的 **[Ndt_Mapping]** 选项，设置 **[app]**，并勾选

- **传感器标定**

  - 计算安装在车辆上的激光雷达与相机的相对位置关系(x, y, z, roll, pitch, yaw)

  - 利用激光雷达数据和相机数据之间的相对位置，可以实现两者数据的融合

    <img src="/home/xiongzh/.config/Typora/typora-user-images/image-20220318174443783.png" alt="image-20220318174443783" style="zoom: 80%;" />

- **3D建图和定位**

  - 使用激光雷达扫描的数据进行3D建图

    ![image-20220318183034562](/home/xiongzh/.config/Typora/typora-user-images/image-20220318183034562.png)


---

### 2. LGSVL









---

### 3. Carla 

`export PYTHONPATH=$PYTHONPATH:~/Carla/PythonAPI/carla/dist/carla-0.9.12-py3.7-linux-x86_64.egg`
