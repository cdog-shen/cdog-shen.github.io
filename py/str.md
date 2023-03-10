# 字符串

基本数据类型之一

定义一个字符串很简单：用`""`或`''`将字符括起来即可

## 字符串也可以当作一个列表来使用

- 用索引来取数据

    `str[int]`可以取到int处索引的单个字符

- for遍历每个字符

    `for word in str:`就是在`str`字符串中依次将字符代入变量word进行运算

## 字符串用法

| 用法及参数                            | 解释                                                                    | 返回值 |
| :------------------------------------ | :---------------------------------------------------------------------- | :----: |
| 通用方法                              | ---                                                                     |  ---   |
| str[int]                              | 索引取值                                                                |  str   |
| len(str)                              | 获取字符串长度                                                          |  int   |
| str1.count(str2)                      | 在str1中统计str2出现的次数                                              |  int   |
|                                       |                                                                         |        |
| 判断类型                              | ---                                                                     |  ---   |
| .isspace()                            | 是否只包含空格                                                          |  bool  |
| .isalnum()                            | 是否全是数字或字母                                                      |  bool  |
| .isalpha()                            | 是否都是字母                                                            |  bool  |
| .isdecimal()                          | 是否全是数字(全角数字)                                                  |  bool  |
| .isdigit()                            | 是否全是数字(全角数字，(1)，\u00b2)                                     |  bool  |
| .isnumeric()                          | 是否全是数字(全角数字，汉字数字)                                        |  bool  |
| .istitle()                            | 是否为标题格式                                                          |  bool  |
| .islower()                            | 是否全为小写                                                            |  bool  |
| .isupper()                            | 是否全大写                                                              |  bool  |
| .startswith(str)                      | 是否以str开头                                                           |  bool  |
| .endswith(str)                        | 是否以str结尾                                                           |  bool  |
|                                       |                                                                         |        |
| 查找/替换                             | ---                                                                     |  ---   |
| .find(str,start=0,end=len(self))      | 在该对象的索引区间内查找str并返回其索引 **(正序左侧数字型)**            |  int   |
| .rfind(str,start=0,end=len(self))     | 在该对象的索引区间内查找str并返回其索引 **(反序右侧数字型)**            |  int   |
| .index(str,start=0,end=len(self))     | 在该对象的索引区间内查找str并返回其索引 **(正序左侧报错型)**            |  int   |
| .rindex(str,start=0,end=len(self))    | 在该对象的索引区间内查找str并返回其索引 **(反序右侧报错型)**            |  int   |
| .replace(old,new,num=self.count(old)) | 替换该对象中的old字符为new字符，num为次数                               |  str   |
|                                       |                                                                         |        |
| 大小写转换                            | ---                                                                     |  ---   |
| .capitalize()                         | 首字母大写                                                              |  str   |
| .title()                              | 每个单词首字母大写                                                      |  str   |
| .lower()                              | 全部小写                                                                |  str   |
| .upper()                              | 全部大写                                                                |  str   |
| .swapcase()                           | 大小写互换                                                              |  str   |
|                                       |                                                                         |        |
| 文本对齐                              | ---                                                                     |  ---   |
| .ljust(width)                         | **左**对齐并用`space`补充长度与`width`相同                              |  str   |
| .rjust(width)                         | **右**对齐并用`space`补充长度与`width`相同                              |  str   |
| .center(width)                        | **居中**对齐并用`space`补充长度与`width`相同                            |  str   |
| .zfill(width)                         | 在左侧添加"0"至width长度                                                |  str   |
|                                       |                                                                         |        |
| 去除空白字符(" ","\n","\t","\t","\r") | ---                                                                     |  ---   |
| .strip()                              | 截去**两**边空白字符                                                    |  str   |
| .lstrip()                             | 截去**左**边空白字符                                                    |  str   |
| .rstrip()                             | 截去**右**边空白字符                                                    |  str   |
|                                       |                                                                         |        |
| 拆分和连接                            | ---                                                                     |  ---   |
| .partition(str)                       | 拆分成三部分("str前","str","str后")                                     | tuple  |
| .rpartition(str)                      | 拆分成三部分("str后","str","str前")                                     | tuple  |
| .split(sep="",num)                    | 以str为分隔符(str默认为'\r','\t','\n',' ')，从左至右分割num次           |  list  |
| .splitlines()                         | 以行('\r','\n','\r\n')分割，获取一个包含各行的列表                      |  list  |
| .join(data)                           | 以自身为 ***分割符***，将`data`中的所有元素的字符串形式合并成新的字符串 |  str   |
| 其他                                  | ---                                                                     |  ---   |
| .encode("(编码类型)")                 | 对字符串进行解码                                                        |  str   |

## 转义字符

| 字符  | 转义       |
| :---: | :--------- |
| "\\"  | 反斜杠/    |
| "\'"  | 单引号'    |
| "\""  | 双引号"    |
| "\t"  | 横向制表符 |
| "\r"  | 回车       |
| "\n"  | 换行       |
