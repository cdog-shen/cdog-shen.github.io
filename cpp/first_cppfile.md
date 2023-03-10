# 第一个CPP文件

## 面向过程的C++程序

下面来通过第一个.cpp文件来了解其大概结构

```c++
#include <iostream> //包含头文件
using namespace std; //C++命名空间
int max(int x, int y) //自定义函数体
{
    int z; //变量定义
    if (x > y) //if判断
        z = x; //if的true
    else //if的else
        z = y; //else的true
    return z; //该函数返回值
}

int main(int argc, char const *argv[]) //主函数定义
{
    int a, b, m; //定义三个整形
    cin >> a >> b; //接收键盘输入
    m = max(a, b); //第一种函数调用形式
    cout << "max = " << max(a, b) << "\n"; //第二种函数调用形式
    cin >> m; //赋值断点而已
    return 0; //主函数返回值
}
```

头文件就像python中的模块, 内部含有很多的函数和类, 但C++的每一个函数都需要被导入,(不同于python, python的内建函数是自动由解释器导入)
`<>`符号也可以用`""`代替，不过使用`<>`会优先查找解释器$Path下的文件
`""`主要是用来导入自己写的头文件

命名空间: 使用命名空间的目的是对标识符的名称进行本地化，以避免命名冲突。在C++中，变量、函数和类都是大量存在的。如果没有命名空间，这些变量、函数、类的名称将都存在于全局命名空间中，会导致很多冲突。

自定义函数: 有点像python中的`def`关键字(就是)

主函数体: C++主程序所需要的主函数, 程序的开始就是`main`函数的第一条语句, 在C++中, 主函数的返回值必须是`整形`

cout: 在C++命名空间的函数, 类似于`printf`

cin: 在C++命名空间的函数, 起到输入的作用(输入流对象)

>>: 提取运算符

<<: 插入运算符

g++编译器会从上到下编译程序来执行，如果上方出现了没有定义或声明的量，就会出现调用错误(这一点与python解释器非常相似)所以，如果上方代码将`main`和`max`函数互换位置，则需要添加一行代码

```c++
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int max(int x, int y); //新增的代码，用来提前声明函数 max
    int a, b, m;
    cin >> a >> b;
    m = max(a, b);
    cout << "max = " << max(a, b) << "\n";
    cin >> m;
    return 0;
}

int max(int x, int y)
{
    int z;
    if (x > y)
        z = x;
    else
        z = y;
    return z;
}
```

- `int max(int x, int y);`该行意思：

    声明函数max，值为`int`型，有两个参数，x为`int`型，y为`int`型

由于编译的顺序性, 声明函数要写在调用之前

## 包含类的C++程序

```c++
#include <iostream>
using namespace std;
class Student //创建类
{
private: //私有部分
    int num, score; //属性定义

public:            //公有部分
    void setdata() // 方法定义
    {
        cin >> num;
        cin >> score;
    }
    void display() // 方法定义
    {
        cout << "num=" << num << endl;
        cout << "score=" << score << endl;
    }
};

Student stud1, stud2; //创建实例

int main(int argc, char const *argv[]) //主函数
{
    /*-主函数位置，调用方法-*/
    stud1.setdata();
    stud2.setdata();
    stud1.display();
    stud2.display();
    return 0;
}

```

这是一个包含类的C++程序

类的关键字`class`与python相同，但是定义方法不太一样，公有和私有直接通过关键字`public`和`private`来区分

创建对象就如同创建变量一样，用其类名来创建(也可以把创建变量本质上当成创建一个对应的对象一样)

调用方法与python相同

## 关于书本

这里有我在看过书之后自己的一些见解和注意事项

- 第一个问题---有关if

    书中很喜欢把if写成这样的嵌套形式

    比如这最大值函数：

    ```c++
    int max(int x, int y) //我的写法
    {
        int z;
        if (x > y) //if语句之后会换行
            z = x;
        else
            z = y;
        return z;
    }

    int max(int x, int y) //书中的写法
    {
        int z;
        if (x > y) z = x;
            else z = y;
        return z;
    }
    ```

    我比较喜欢写成具有明确缩进格式的样子，主要也是受python语法的影响，但个人认为这样的逻辑更为清晰
