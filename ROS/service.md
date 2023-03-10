# 服务通信

服务通信模式就正是如现在互联网上的标准模式一样, 客户机先发送一个GET请求, 服务器给予回应, 两者都具有收发能力, 对于ROS来说, 每个节点都相当与一个服务器/客户机

服务通信适用于适时性的,具有一定逻辑处理需求的场景

## 实现流程

* 1.服务器在core注册信息---话题信息(或者说是请求信息)
* 2.客户端在core注册需求---话题信息
* 3.core匹配话题(请求)并给客户端匹配地址
* 4.客户端发送请求
* 5.服务器返回结果

**注意**: 服务通信是要保证启动顺序的; 服务通信互相交换的叫做数据载体(可以自定义)

## 自定义srv文件

服务通信的srv就是所谓的数据载体, 定义数据载体是方便服务器与客户端之间的通信

但请求和返回并不是一样的数据, srv文件通常是被分为上下两部分: **客户使用部分** 和 **服务器使用部分** 其上下用 `---`分割开

这里我们使用一个数据求和的例子来演示服务通信

### 配置文件调整

#### package.xml

因为srv与msg本质上都是属于`std_msgs`所以都要依赖于这个

当然还包括: `message_generation` `message_runtime`

#### CMakeList.txt

* find_package

    `+` message_generation

* catkin_package

    `+` message_runtime

* add_service_file

    `+` `<filename>`.srv

### 服务端实现

前面都是正常顺序, 建节点, 建句柄

然后就是用句柄建立server对象

```cpp
ros::ServiceServer <obj_name> = <nodeHandle_name>.advertiseService("<toppic_name>",<recallFunction_name>);
```

可以看到, 服务端想要持续运行, 接收请求是需要有回调函数的

```cpp
bool <recallFunction_name>(srv_creater::nums::Request &request_obj,
                            srv_creater::nums::Response &respond_obj)
{
    int num1 = request_obj.num1;
    int num2 = request_obj.num2;
    int sum = num1 + num2;
    respond_obj.sum = sum;

    return true;
}
```

回调函数的写法就是这样, 与话题消息大同小异, 可以推理出其意思

当然, 有了回调函数就有spin, 要加再主逻辑最后

### 客户端实现

客户对象实现

```cpp
    ros::ServiceClient <obj_name> = <nodeHandle_name>.serviceClient< <srv_namespace>::<srv> >("<topic_name>");
```

#### 请求连接部分

```cpp
srv_creater::nums user; // 创建消息对象

// 调用消息对象的request部分的属性
user.request.num1 = 100; 
user.request.num2 = 200;

bool flag = client.call(user); // 调用client的call方法发送请求

if (flag) // 获取请求的返回值
{
    ROS_INFO("get respond = %d",user.response.sum); // 输出消息返回值中的sum
} 
else
{
    ROS_INFO("respond false");
}
```
