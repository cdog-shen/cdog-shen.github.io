# hping3

这个工具是面向命令行的, 用于生成/解析TCP/IP协议数据包汇编/分析的开源工具

hping3是最新版本, 支持TCP UDP ICMP RAW-IP协议, 具有跟踪路由的模式, 能够在覆盖的信道之间发送文件以及许多其他功能

hping可以定制数据包的各个部分, 因此可以对目标主机进行灵活探测

- 实验靶机:

    Metasploitable2 ==> 192.168.48.134

    Windows7 ==> 192.168.48.131

- 实验项目(均在kali-root下运行):

    `hping3 --help`    显示用法

    `hping3 -I <网卡名称> -S <ip address> -p <port num>`    对指定主机的指定端口进行扫描(这个用法与ping命令大同小异)

    `这里留个空`    对指定主机进行DoS攻击