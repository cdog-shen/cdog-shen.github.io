# list--列表

列表，在其它语言中又成为`数组`，被专门用来储蓄一系列数据而生

用`[]`来定义，每个数据之间用`,`来隔开

**列表的索引从"0"开始(就是数据在列表中的位置)**

|       |       |       |       |
| :---: | :---: | :---: | :---: |
|   [   |   1   |   2   |   ]   |
| 索引: |   0   |   1   |   /   |

如果调用的值在列表中没有，解释器会报错

常用列表操作函数:

| 操作及用法              | 解释                                                        | 返回值类型 |
| :---------------------- | :---------------------------------------------------------- | :--------: |
| len(list)               | 返回列表长度                                                |    int     |
| list.count(data)        | 返回`data`的出现次数                                        |    int     |
| list[int]               | 返回索引处的值(如果对其进行重新赋值,，则会修改当前索引的值) |     *      |
| list.index(data)        | 返回`data`第一次出现的索引                                  |    int     |
| del list[int]           | 删除指定索引的数据                                          |    list    |
| list.pop(int)           | 删除指定索引的数据(`int`留空就删除最后一个)                 |    list    |
| list.remove(data)       | 删除第一个出现的`data`                                      |    list    |
| list.clear()            | 清空列表                                                    |    list    |
| list.insert(index,data) | 在`index`处插入数据`data`                                   |    list    |
| list.append(data)       | 在结尾追加数据`data`                                        |    list    |
| list1.extend(list2)     | 将`list2`追加到`list1`的结尾                                |    list    |
| list.sort()             | 升序排列                                                    |    list    |
| list.sort(reverse=True) | 降序排列                                                    |    list    |
| list.reverse()          | 反转/逆序                                                   |    list    |

***`del` 关键字实际上是用于将某个数据从内存中删除***
