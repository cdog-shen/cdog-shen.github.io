# 在VScode中配置C/C++环境

- 所需程序包:

    [VScode-WindowNT](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)
    - code拓展:

        vscode-icon(code图标, 增加辨识度)

        C/C++(语言拓展, 支持代码补全和高亮)

        Rainier(颜色主题)

        Path Intellisense(路径联想)

        Bracket Pair Colorizer 2(括号颜色成对)

        indent-rainbow(彩虹缩进)

        Code Runner(代码运行器)

        Chinese (Simplified) (简体中文) Language Pack for Visual Studio Code(官方简中包)

        CMake(车队所需的编译环境)

    [MinGW编译器-WindowNT](https://sourceforge.net/projects/mingw/)(安装时记住安装路径)

## 当你完全安装完后需要的设置

在VScode中的设置中搜索`run in terminal`找到下条并勾选

![run_in_terminal](source/run_in_terminal.png)

新建一个cpp文件, 用vscode打开, 进入调试界面

![lunch](source/launch.png)

创建launch.json文件

![GDB](source/GDB.png)

编写一个hello world程序

```c++
#include <iostream>  //头文件iostream
using namespace std; //C++命名空间std
int main()
{
    cout << "Hello world";
    return 0;
}
```

按下`F5`开始测试

如果不能在集成终端中看到输出结果的话, 进入`launch.json`文件更改键值`externalConsole`为`true`即可
