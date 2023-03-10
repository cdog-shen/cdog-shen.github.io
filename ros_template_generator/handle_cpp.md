# 针对handle.cpp文件的修改

## 第 *3* 条修改

在更改头文件中的属性定义之后, 要在cpp中进行方法改写和补充

* 首先要更改的是参数加载方法

    添加与yaml中对应的**if**语句

    ![parameter_loader](img/parameter_loader_handle_cpp.jpg)

    * 从上到下五条修改依次是:

        yaml的**标识符**

        hpp中的**话题属性**

        yaml的**话题名**

        yaml的**标识符**(用于异常提示信息)

        hpp中的**话题属性**(用于异常提示信息)

* 然后要对发布和订阅方法进行添加

    ![pubsub](img/pubsub_object_handle_cpp.jpg)

    具体做法就是在对应的方法中添加固定格式的语句

    * sub

        ```cpp
        定义的sub对象 = nodeHandle_.subscribe(消息类型属性, 1, &test_classHandle::callback名称, this);
        ```

    * pub

        ```cpp
        定义的pub对象 = nodeHandle_.advertise<使用的消息类型>(消息类型属性, 1);
        ```

* 添加subscriber所需的callback

    ![callbackdef](img/callbackdef_handle_cpp.jpg)

    ```cpp
    void test_classHandle::*handle中定义的callback名称*(const 数据类型 &数据变量名) {
    test_object_.setData(数据变量名); //此处setData函数是保存数据函数, 每一种消息对应一个
    }
    ```

    在定义完成后, IDE必然会对`test_object_.setData`进行报错, 因为这个新的函数并没有被定义, 所以下一步就是新增这个函数(位于object.hpp)

## 第 *7* 条更改

* 为发送操作更新sent方法

    就是在sentMsg方法中再添加一个对应消息类型的获取信息的方法就行

    ```cpp
    发布者对象.publish(test_object_.getData()); //getData就是获取操作
    ```
