# dnsmap

DNS域名暴力穷举工具

通过自定字典或内置字典来对主域名的子域名进行探测并且对其进行定位

- 使用实例:

    `dnsmap <url>` 内置字典探测

    `dnsmap <url> -w <wordlist_filepath> -r <resault_filepath>`对域名采取字典内子域名的搭配组合进行穷举, 并将所得结果保存在对应文件内

    还有其他选项可以使用: `-d <time>`设置延迟 `-i <ignore ip>`设置忽略的ip(通常用于忽略虚拟ip)