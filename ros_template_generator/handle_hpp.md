# 针对handle.hpp文件的修改

## 第 *2* 条修改

* 先对test_CHandle(class)进行更改

    * 添加私有对象/属性

        对应的 **subscriber** 和 **publisher**

        ![objdef](img/objdef_object_handle_hpp.jpg)

        需要的使用的 **话题属性**

        ![topicname](img/topicname_object_handle_hpp.jpg)

        用于接收的 **回调函数**

        ![callback](img/callback_object_handle_hpp.jpg)

        ***注意, callback调入消息类型的时候如果代码补全中没有你所需要的对象, 你就要自行检查一下`CMakeList.txt是不是少包`和`是否object.hpp少include头文件了`***
