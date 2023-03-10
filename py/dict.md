# 字典

字典也可以用来储存多个数据

由于具有`键`和`值`的概念，字典通常用于存储某个物体的具体信息

- 与列表不同

    `列表`是**有序**的
    `字典`是**无序**的

    原因:`列表`中的数据存储位置使用**索引**表示的，而在`字典`中是用**键**表示的

字典的定义：`{}`

- 字典的存储方式 **键:值(key:value)**

    key是索引，必须是唯一的，且只能是**数字，字符串，元组**
    value是值
    key和value之间用`:`隔开
    不同的数据之间用`,`分隔符隔开

## 字典的使用

同tuple和list一样，dict也可以用`dict[key]`的方式来调取、修改、添加数据

|操作及用法|解释|返回值|
|:-|:-|:-:|
|dict[key]|调取键的值|*|
|dick[key] = value|新建/更改值|dict|
|dict.pop(key)|删除键值对|dict|
|len(dick)|统计字典长度|int|
|dict1.update(dict2)|用dict2更新dict1|dict|
|dict.clear()|清空字典|dict|

## for遍历字典

用for遍历字典时，获取到的是字典的key

例如:

```python
adict = {"name":"ztr","age":17}

for k in adict:
    print("键:%s 值:%s" %(k,adict[k]))
```
