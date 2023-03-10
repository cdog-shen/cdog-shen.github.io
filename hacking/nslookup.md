# nslookup查询DNS

这个命令通常是在网络故障时来查询DNS记录, 来判断域名解析服务是否正常, 是诊断工具

- 使用实例

    最常用的就是查询域名的A记录`nslookup <url> <dns-server>`, 如果没有指定dns服务器, 就用默认服务器

    ![basic](img/nslookup.png)

    可以看出初始DNS的位置, 并对比GOOGLE公共DNS, 解析结果相同

    查询其他记录`nslookup -type=<type-code> <url> <dns-server>`

    此处type-code可以是一下几个

    <!-- |type-code|类型|
    |:-:|:-:|
    |A|地址记录v4|
    |AAAA|地址记录v6|
    |AFSDB|Andrew文件系统数据库服务器记录|
    |ATMA|ATM地址记录|
    |MX|邮件服务器记录|
    |SRV|TCP服务器记录| -->

    ![type](img/ns_type.png)