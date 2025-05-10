# A. Network Configuration and Interface Commands

ipconfig
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /flushdns
ipconfig /displaydns
getmac
hostname
netsh interface ip show config
wmic nic get name,macaddress
netsh wlan show interfaces
netsh wlan show profiles

# B. Network Testing and Diagnostics

ping
ping 126.192.1.1
tracert
tracert 126.192.1.1
pathping
telnet
nslookup
ftp
arp -a
nbstat
route print
setspn

# C. Network Statistics and Monitoring

netstat
netstat -a
netstat -b
netstat -n
netstat -o
netstat -r
netstat -s
netstat -e
tasklist
taskkill
perfmon
wmic path win32_networkadapter where (NetEnabled='true') get Name, 
MACAddress, Speed

# D. Network Resource Management

net
net use
net view
net user
net localgroup
net share
net session
net file
net config

# E. Advanced & Security Commands

netsh
netsh interface
netsh firewall
netsh wlan
netsh int tcp show global
systeminfo
sc
shutdown -i
mstsc
netstat -anob