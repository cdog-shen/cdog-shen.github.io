# ROS相关命令

## 1.新建公文包

```sh
catkin_create_pkg <package_name> <dependence_name>
```

## 2.包管理

用apt进行包管理

### 安装包

```sh
sudo apt install ros-melodic-<dependence_name>
```

### 删除包

```sh
sudo apt remove ros-melodic-<dependence_name>
```

### 查询包

列出所有包

```sh
rospack list
```

查找包是否存在(会返回路径)

```sh
rospack find <dependence_name>
```

进入包的目录

```sh
roscd <dependence_name>
```

在包目录ls

```sh
rosls <dependence_name>
```

查找网路可安装的包

```sh
apt search ros-melodic-<dependence_name>
```

### 改包

用vim编辑

```sh
rosed <dependence_name> <file_name>
```

## 执行

启动ROS系统核心(核心启动后才能进行节点通信)

共三个系统会被启动

* ros master
* ros 参数服务器
* rosout 日志节点

```sh
roscore -p <port>
```

运行单个程序包

```sh
rosrun  <package_name> <file_name>/<node_name>
```

运行一个包内的launch文件

```sh
roslaunch <package_name> <launch_file_name>
```

