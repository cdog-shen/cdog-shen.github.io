# SMB(Server Message Box)协议扫描

利用msf来进行smb协议的的扫描, 可以快速得知目标主机的操作系统内核版本, 补丁版本, 快速检测易受到攻击的设备

- 靶机环境:

    Windows 7 ==>192.168.48.131

    ![win-v](img/win7_version.png)

    Metasploitable2 ==> 192.168.48.134

    ![m-v](img/metasploitable_version.png)

- 扫描实例:

    `search smb`查找smb可用扫描模块

    ![smb](img/search_smb_ans.png)

    使用smb_version的版本扫描器

    扫描结果:

    ![smb_r](img/smb_result.png)

    可以看出Windows的系统版本被完全识别(包括系统补丁版本SP1), metasploitable由于是魔改系统, 不能识别出准确体统类型, 但显示是Debian类型, 结果都正确