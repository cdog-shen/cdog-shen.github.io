# Service version服务版本扫描

记得`nmap -sV`吗, sV就是Service version的简称今天主要是对Metasploitable2主机的ssh版本进行扫描

- 靶机环境:

    Metasploitable2 ==> 192.168.48.134

- 实例测试:

    话不多说直接放图

    ![svs_result](img/svs_result.png)

    模块:auxiliary/scanner/ssh/ssh_version

    msf的模块扫描的信息更全面, 也更快, 但只能单个服务的测试

    nmap的结果就相对概括一点了, 但两者的信息都还是一样的, 大版本号都一致

    因此可以先用nmap去看一下那些服务是突破口, 在用msf去扫描具体版本号确定漏洞和攻击载荷