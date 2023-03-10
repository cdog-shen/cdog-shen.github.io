# Arping的使用方法

`Arp`是`地址解析协议`一词的英文缩写, 在同一网络下, 用户可以通过ip地址来获得目标主机的MAC

Arping, 用来向局域网内的其他主机发送ARP请求的指令, 可以用来测试局域网内的某个ip地址是否被禁用或者是否在线

- 实验靶机:

    windows7 ==> 192.168.48.131

- 使用实例:

    `sudo arping <ip address>` 基本用法, 对指定主机发送arp请求并获取其MAC

    ![arping](img/arping-regu.png)

    ![ans](img/arping-ans.png)

    还有其他可选参数:`-c <count> 指定请求数量` `-w <timeforsecond> 指定发送几秒`

    其他参数设置

    ![help](img/arping-help.png)

- 与其他工具的用法联系

    可以与`aireplay-ng`一起使用对已知网络环境发动攻击(因为已知的网络环境的网关地址基本上就是路由地址, 可以直接通过arping指令直接获取其MAC, 然后利用aireplay-ng指令发动洪水攻击)