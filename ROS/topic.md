# 话题通信

话题topic通信机制是一种订阅发布模式, 一端是发送端, 一段是接收端

话题通信有三大要素: 发送端, 接收端, 话题

适用于 ***需要实时更新, 少逻辑处理的数据场景***

## 理论模型

话题通信实现模型是比较复杂的，该模型如下图所示,该模型中涉及到三个角色:

* ROS Master (管理者)
* Talker (发布者)
* Listener (订阅者)

![topic](img/topic.png)

ROS Master 负责保管 Talker 和 Listener 注册的信息，并匹配话题相同的 Talker 与 Listener，帮助 Talker 与 Listener 建立连接，连接建立后，Talker 可以发布消息，且发布的消息会被 Listener 订阅

最后的整个 TCP 通信是基于话题通过 RPC 建立起来的, 所以订阅和发布的话题相同, 不同语言的节点也可以进行通信

## 整个流程步骤

* 0.Talker注册

    Talker启动后，会通过RPC在 ROS Master 中注册自身信息，其中包含所发布消息的话题名称。ROS Master 会将节点的注册信息加入到注册表中。

* 1.Listener注册

    Listener启动后，也会通过RPC在 ROS Master 中注册自身信息，包含需要订阅消息的话题名。ROS Master 会将节点的注册信息加入到注册表中。

* 2.ROS Master实现信息匹配

    ROS Master 会根据注册表中的信息匹配Talker 和 Listener，并通过 RPC 向 Listener 发送 Talker 的 RPC 地址信息。

* 3.Listener向Talker发送请求

    Listener 根据接收到的 RPC 地址，通过 RPC 向 Talker 发送连接请求，传输订阅的话题名称、消息类型以及通信协议(TCP/UDP)。

* 4.Talker确认请求

    Talker 接收到 Listener 的请求后，也是通过 RPC 向 Listener 确认连接信息，并发送自身的 TCP 地址信息。

* 5.Listener与Talker件里连接

    Listener 根据步骤4 返回的消息使用 TCP 与 Talker 建立网络连接。

* 6.Talker向Listener发送消息

    连接建立后，Talker 开始向 Listener 发布消息。

## 注意

* 1.整个过程的前五步是要通过master来建立 RPC 调用, 取得了 TCP/UDP 地址以后再建立更高效的 TCP/UDP 协议通信

## 基本操作

对于三个角色 Talker Listener Master

其中Master由roscore来控制, 并不需要程序员来操心, 我们要注意的就是 (Talker建立) (Listener建立) (Topic确定) (要发送什么message)

所以就有了一个大致流程:

* 编写Talker
* 编写Listener
* 编辑配置文件
* 编译并执行

## 源码实例

### C++实例

#### Talker实例

编写一个Talker有五个重要步骤:

* 1.包含头文件
* 2.ros节点初始化
* 3.创建节点句柄
* 4.创建预发布者对象
* 5.编写发布逻辑并发送数据

```c++
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
// a publisher code

int main(int argc, char *argv[])
{
    // initialize ros node
    ros::init(argc,argv,"talker");
    // set node handle (object)
    ros::NodeHandle a_talk;
    // set publisher (object)
    ros::Publisher pub = a_talk.advertise<std_msgs::String>("test_talk",10,false);
    // advertise messages (loop)
        // create message (obiect)
        std_msgs::String msg;
        // set send rate (object)(Hz)
        ros::Rate rate(10);
        // set num of message
        int count = 0;
        // create send loop
        while (ros::ok())
        {
            // num change
            count++;
            // set a StrStream object
            std::stringstream message;
            message  << "hello" << count;
            // set msg
            msg.data = message.str();
            // publish
            pub.publish(msg);
            // output info
            ROS_INFO("publish succeed");
            // rate useage
            rate.sleep();
        }
        
    return 0;
}

```

* 整个代码的解释:

    ```txt
    初始化ros节点

    实例化一个NodeHandle对象(a_talk)
        ---> 实例化一个Publisher对象(pub)并定义其发送的目标为(a_talk)句柄的(test_talk)话题, 信息类型为<std_msgs::String>
            ---> 定义一个msg的标准信息
                ---> 发送循环体{给msg的data属性定义为"hello"}
                    ---> 调用pub对象的publish方法,参数为(msg)
    ```

#### Listener实例

编写一个Listener有五个重要步骤:

* 1.包含头文件
* 2.ros节点初始化
* 3.创建节点句柄
* 4.编写回调函数处理接收信息
* 5.创建订阅者对象

```c++
# include "ros/ros.h"
# include "std_msgs/String.h"

void domsg(const std_msgs::String::ConstPtr &msg){    // recall function
    ROS_INFO("Linstener is linstening %s",msg->data.c_str());
}


int main(int argc, char *argv[])
{
    // initalize ros node
    ros::init(argc,argv,"linstener");
    // set handler (object)
    ros::NodeHandle a_talk;
    // create Subscriber (object)
    ros::Subscriber sub = a_talk.subscribe("test_talk",10,domsg);
    // a spin give a gap to process the messages from recall function
    ros::spin();

    return 0;
}
```

我们发现, 订阅方的代码中并没有类似发送动作的代码`pub.publish(msg);`

这就可以想象成一个投篮者,篮筐,篮球的关系, 无论投中(被接收)与否, 投篮者(Publisher)只是投送篮球(msg), 但篮球(msg)被接收后, 篮筐(Subscriber)都要进行处理(recall function)

可以说 Publisher 是主动的, Subscriber 是被动方
