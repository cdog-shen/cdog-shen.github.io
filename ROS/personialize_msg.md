# 自定义消息类型

由于std_msgs库中的标准消息格式只包含基本数据类型中的其中一类, 功能极度单一, 所以我们在使用时要自己创建消息类型来生成包含数据量更丰富的消息

创建一个自定义msg需要的流程:

* 1.**按照格式**创建`msg`文件
* 2.编辑配置文件
* 3.编译生成可调用的中间文件

在本文中, 我将利用某个个人信息来创建一个消息类型

## 定义msg文件

首先在公文包下创建新目录`msg`

新建`Person.msg`

如定义变量(或者是结构体)一般定义消息

`数据类型 标识符`

### 消息类型

int型: `int8` `int16` `int32` `int64` `uint8` `uint16` `uint32` `uint64`

float型: `float32` `float64`

char型: char

str型: string

bool型:bool

时间型:`time` `duration`

数组型: `variable-length array[]` `and fixed-length array[C]`

其他型: `other msg files`

空型: `empty`

## 修改配置

### package.xml

在依赖标识处添加两行

![xml](img/pmsg_xml.png)

```xml
    <build_depend>message_generation</build_depend>
    <exec_depend>message_runtime</exec_depend>
```

### CMakeLists.txt

从上到下依次更改

* find_package当中

    **+** message_generation

* add_message_files中

    **-** 所有#

    **-** Message1.msg

    **-** Message2.msg

    **+** Person.msg

* generate_messages中

    **-** 所有#

* catkin_package中

  * CATKIN_DEPENDS前后

    **-** #

    **+** message_runtime

## 自定义消息调用

调用时也就像正常消息格式一样调用, 只不过需要不同的头文件, 而这些头文集都是你后期生成的, 如果想在vscode中使用, 需要去额外调整一下`.vscode/c_cpp_properties.json`里面的`path`

## 准备工作---更新vscode的includepath

我们需要在includepath的条目下添加你新生成的消息头文件的绝对路径

通常路径为`<work space>/devel/include/**`

## 调用

### 发布方简单实例实现

#### 导入head

由于有了新的消息包, 原有的`std_msgs`就不再需要了重新导入一个以下格式的head

```c++
#inclue "<公文包名称>/<msg下文件名>"
```

并且要对相关包含消息类型的地方进行更改

比如advertis语句中`<>`内的消息类型要改为

```c++
公文包名::msg下文件名
```

创建一个消息实例

```c++
公文包名::msg下文件名 标识符;
```

修改其内部数值时, 就等同于修改其属性

```c++
标识符.属性名 == <对应类型数值>;
```

### 订阅方简单实例

#### 导入

同样要和接收方一样include消息包

#### 接收

接收消息的部分(也就是回调函数部分)要进行比较大的改动

```cpp
void get_person(const puber_suber::Person::ConstPtr& person)
{
    ROS_INFO("message get : %s,%d,%.2f,%s",person->age,person->age,person->height,person->sex);
}
```

可以解构为以下的格式

```xml
void <回调函数名称>(const <调用的消息所在包::消息类型::ConstPtr>& <指定标识符>){
    ROS_INFO("message get : %s,%d,%.2f",<指定标识符>-><消息内部属性>);
}
```

## 编译

由于编译时涉及了新的依赖包`message_generater`, 就要考虑编译的先后性了

修改CMakeLists.txt中, 位于`add_executable`条例和`target_link_libraries`条例之间的`add_dependencies`部分

* 具体修改方法:

    add_dependencies(<自定义的链接名> ${PROJECT_NAME}_generate_message_cpp)

## 推荐使用方法

在自定义消息之后, 只有改公文包内才可以使用自己定义的消息, 别的公文包则不能使用

我们的做法是, 单独创建一个公文包, 不放置任何源码, 仅仅是用来进行自定义消息定义, 如果其他包要调用他, 就要在其`package.xml`里面添加这个公文包(或者在创建公文包时进行添加), 再在对应的.cpp文件的#include中, 就可以对消息进行更改和发送了

同样, 在消息所在的包中, 只需要配置与消息生成(编译)相关的选项即可
