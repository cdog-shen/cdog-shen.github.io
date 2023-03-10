# Cisco网络设备维护操作

<details>
<summary> 交换机配置 </summary>

* 模式转换命令

用户模式----特权模式,使用命令"enable"

特权模式----全局配置模式,使用命令"configt"

全局配置模式----接口模式,使用命令"interface+接口类型+接口号"

全局配置模式----线控模式,使用命令"line+接口类型+接口号"

注:
用户模式:查看初始化的信息.

特权模式:查看所有信息、调试、保存配置信息

全局模式：配置所有信息、针对整个路由器或

交换机的所有接口

接口模式：针对某一个接口的配置

线控模式：对路由器进行控制的接口配置

* 配置命令

show running config 显示所有的配置

show versin 显示版本号和寄存器值

shut down 关闭接口

no shutdown 打开接口

ip add +ip地址配置IP地址

secondary+IP地址为接口配置第二个IP地址

show interface+接口类型+接口号查看接口管理性

show controllers interface 查看接口是否有DCE电缆

show history 查看历史记录

show terminal 查看终端记录大小

hostname+主机名配置路由器或交换机的标识

config memory 修改保存在NVRAM中的启动配置

exec timeout 0 0 设置控制台会话超时为0

service password-encryptin 手工加密所有密码

enable password +密码配置明文密码

ena sec +密码配置密文密码

line vty 0 4/15 进入telnet接口

password +密码配置telnet密码

line aux 0 进入AUX接口

password +密码配置密码

line con 0 进入CON接口

password +密码配置密码

bandwidth+数字配置带宽

no ip address 删除已配置的IP地址

show startup config 查看NVRAM中的配置信息

copy run-config atartup config 保存信息到NVRAM

write 保存信息到NVRAM

erase startup-config 清除NVRAM中的配置信息

show ip interface brief 查看接口的谪要信息

banner motd # +信息 + # 配置路由器或交换机的描素信息

description+信息配置接口听描素信息

vlan database 进入VLAN数据库模式

vlan +vlan号+ 名称创建VLAN

switchport access vlan +vlan号为VLAN为配接口

interface vlan +vlan号进入VLAN接口模式

ip add +ip地址为VLAN配置管理IP地址

vtp+service/tracsparent/client 配置SW的VTP工作模式

vtp +domain+域名配置SW的VTP域名

vtp +password +密码配置SW的密码

switchport mode trunk 启用中继

no vlan +vlan号删除VLAN

show spamming-tree vlan +vlan号查看VLA怕生成树议

</details>

---

<details>
<summary> 路由器配置命令 </summary>

ip route+非直连网段+子网掩码+下一跳地址配置静态/默认路由

show ip route 查看路由表

show protocols 显示出所有的被动路由协议和接口上哪些协议被设置

show ip protocols 显示了被配置在路由器上的路由选择协议,同时给出了在路由选择协议中使用的定时器等信息

router rip 激活RIP协议

network +直连网段发布直连网段

interface lookback 0 激活逻辑接口

passive-interface +接口类型+接口号配置接口为被动模式

debug ip +协议动态查看路由更新信息

undebug all 关闭所有DEBUG信息

router eigrp +as号激活EIGRP路由协议

network +网段+子网掩码发布直连网段

show ip eigrp neighbors 查看邻居表

show ip eigrp topology 查看拓扑表

show ip eigrp traffic 查看发送包数量

router ospf +process-ID 激活OSPF协议

network+直连网段+area+区域号发布直连网段

show ip ospf 显示OSPF的进程号和ROUTER-ID

encapsulation+封装格式更改封装格式

no ip admain-lookup 关闭路由器的域名查找

ip routing 在三层交换机上启用路由功能

show user 查看SW的在线用户

clear line +线路号清除线路

</details>

---

