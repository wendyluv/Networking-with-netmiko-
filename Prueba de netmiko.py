# Prueba basica de netmiko


from netmiko import ConnectHandler as CH

cisco = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.1',
	'username': 'admin',
	'password' : 'cisco'}
	
net_connect = CH(**cisco)
net_connect.find_prompt()
print(net_connect.send_command("show running"))
input()

#configuracion basica del dipsositivo
'''
enable 
config terminal
hostname r
ip domain-name cisco.com
enable secret cisco
crypto key generate rsa
1024
username admin secret cisco
line vty 0 4
password cisco
login
logi local
logging s
transport input ssh
exit
line console 0 
password cisco
login
exit
interface fa 0/0 
ip address 192.168.0.1 255.255.255.0
no shut
exit
'''