 # 海狗的笔记---基于rslidar的[readme](https://gitee.com/wang_fenging/rslidar_sdk?_from=gitee_search#/wang_fenging/rslidar_sdk/blob/release/doc/intro/parameter_intro_cn.md)和[docs](https://gitee.com/wang_fenging/rslidar_sdk/tree/release/doc)

 ## 工程介绍

rslidar_sdk 为速腾聚创在Ubuntu环境下的雷达驱动软件包，包括了雷达驱动内核， ROS拓展功能，ROS2拓展功能，Protobuf-UDP通信拓展功能。对于没有二次开发需求的用户，或是想直接使用ROS或ROS2进行二次开发的用户，可直接使用本软件包， 配合ROS或ROS2自带的RVIZ可视化工具即可查看点云。 对于有更深一步二次开发需求，想将雷达驱动集成到自己工程内的客户， 请参考雷达驱动内核的相关文档，直接使用内核rs_driver进行二次开发。

## 可用规格

### 雷达型号

- RS16
- RS32
-RSBP
- RS128
- RS80
- RSM1-B3
- RSHELIOS

### 可用点类型支持

- XYZI

    x-x轴, y-y轴, z-z轴, intensity-反射强度

- XYZIRT

    x-x轴, y-y轴, z-z轴, intensity-反射强度, ring-检测环, timestamp-时间戳

## 所需依赖

用以下命令即可用apt包管理工具解决依赖问题

```shell
sudo apt-get update && sudo apt-get install -y libyaml-cpp-dev libpcap-dev libprotobuf-dev protobuf-compiler
```

## 编译与运行

### 直接编译

采用cmake来直接对项目进行直接编译：按照如下指令即可编译运行程序。 直接编译也可以使用ROS相关功能(不包括ROS2)，但需要在程序启动前手动启动roscore，启动后手动打开rviz才能看到可视化点云结果。

```shell
cd rslidar_sdk
mkdir build && cd build
cmake .. && make -j4
./rslidar_sdk_node
```

### 依赖于ROS-catkin编译

- 1 打开工程内的CMakeLists.txt文件，将文件顶部的set(COMPILE_METHOD ORIGINAL)改为set(COMPILE_METHOD CATKIN)

    ```shell
    #=======================================
    # Compile setup (ORIGINAL,CATKIN,COLCON)
    #=======================================
    set(COMPILE_METHOD CATKIN)
    ```

- 2 将rslidar_sdk工程目录下的package_ros1.xml文件重命名为package.xml

- 3 新建一个文件夹作为工作空间，然后再新建一个名为src的文件夹, 将rslidar_sdk工程放入src文件夹内

- 4 返回工作空间目录，执行以下命令即可编译&运行

    ```shell
    catkin_make
    source devel/setup.bash
    roslaunch rslidar_sdk start.launch
    ```

## 参数介绍

### common部分

此部分主要是设置消息来源，以及是否发布消息

例码：

```ymal
common:
  msg_source: 1                                                             
  send_packet_ros: false                               
  send_point_cloud_ros: false                           
  send_packet_proto: false                              
  send_point_cloud_proto: false                         
  pcap_path: /home/robosense/lidar.pcap                 
```
