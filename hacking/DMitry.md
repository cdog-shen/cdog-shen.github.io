# DMitry

这是一个用于查询域名/ip的whois信息的工具

常用参数:

![op](img/dmitry_op.png)

这些参数可以像ls命令一样将参数叠加起来

例句: `dmitry -w baidu.com -s -p -f -b -o /home/user/desktop/baidu.out`

意思是: 对baidu.com进行whois查询, 并且进行子域探测,端口扫描,获取banner,并将结果保存在/home/user/desktop/baidu.out文件