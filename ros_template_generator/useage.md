# 有关ros_template_generator的用法讲解

## 生成模板

在项目目录下利用python3+来运行`generate.py`文件, 系统会让你选择所需的模板结构

其包含了两个重要参数:**所选语言: py/c++** **项目属性: package_name object_name class_name**

确定参数之后, 会生成一个以**package_name**为目录名称的公文包, 其当前状态可以直接放入工作区内进行编译操作

* 现在我们假设一个模板公文包:

    * package_name -> test_demo
    * object_name-> test_object
    * class_name -> test_C

执行完成后会生成ros-公文包文件, 其主要目录有三个

* config -> 内含有yaml文件, 主要作用是标记话题名
* include -> 内包含了句柄头文件和类头文件
* src -> 包含主函数,句柄方法定义, 类方法定义

## 将模板改为我们所需的程序

对于1+2+3个文件的更改, 我们想要去直接刨析整个项目的源码显然是比较麻烦的, 因此有一个修改顺序: [1.yaml](yaml.md) -> [2.handle.hpp](handle_hpp.md) -> [3.handle.cpp](handle_cpp.md) -> [4.object.cpp](class_cpp.md) -> [5.object.hpp](class_hpp.md) -> [6.object.cpp](class_cpp.md) -> [7.handle.cpp](handle_cpp.md)

自此, 主要收发框架就算是完成了

要具体对收来的数据进行操作后再发送走, 就在`object.cpp`中给`runAlgorithm()`方法进行编写, 程序所有的数学操作都要在这个函数中进行
