# catkin workspace file system

先来看一个tree

![fs](img/file_sys.png)

其中package目录中还可以有两个不常用文件夹 action(动作格式文件) 和 config(配置信息)

下面将以package为主目录, 以不同目录的方式来详解它们的作用

## ./package.xml

这个文件有那么比较重要的几行(也就这几行有用)

```xml
<?xml version="1.0"?>
<package format="2">
    <name>hello_world</name>    # 这部分会与你的公文包同名
    <version>0.0.0</version>    # 你的包版本
    <description>The hello_world package</description>    # 描述
    <maintainer email="cdog@todo.todo">cdog</maintainer>    # 作者信息
    <license>TODO</license>    # 证书好像是
    <buildtool_depend>catkin</buildtool_depend> # 编译工具
    # 这部分开始非常重要, 下面被我分隔开的都是你创建公文包时选择导入的依赖
    # 构建所需包
    <build_depend>roscpp</build_depend>
    <build_depend>rospy</build_depend>
    <build_depend>std_msgs</build_depend>
    # 建库所需包
    <build_export_depend>roscpp</build_export_depend>
    <build_export_depend>rospy</build_export_depend>
    <build_export_depend>std_msgs</build_export_depend>
    # 运行所需包
    <exec_depend>roscpp</exec_depend>
    <exec_depend>rospy</exec_depend>
    <exec_depend>std_msgs</exec_depend>
    # 如果包名字输入错误或者后续需要添加依赖, 可以在上面添加
        <export>
    </export>
</package>
```

## ./CMakeLists.txt

还是通过注释的方法写出来吧

```txt
cmake_minimum_required(VERSION 3.0.2)    # 编译所需编译器的最低版本
project(hello_world)    # 这部分会与你的公文包同名
```

```txt
# 这部分是你编译时需要的外部依赖
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)
```

```txt
# 为你自己写的文件添加一个可执行属性
add_executable(hello_world src/helloworld_vs.cpp)
# 动态链接此文件到ROS的库中
target_link_libraries(hello_world
  ${catkin_LIBRARIES}
)
# 此处两个hello_world都是自己定义在ROS中的节点名称
```

```txt
# 安装自己的python脚本和指定python3解释器
catkin_install_python(PROGRAMS
  scripts/hwp.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```