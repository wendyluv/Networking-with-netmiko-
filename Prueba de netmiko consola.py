# Prueba basica de netmiko


from netmiko import ConnectHandler as CH

cisco = {
	'device_type': 'cisco_ios_serial',
	'serial_settings':{'port':'COM4'},
	'password' : ''}
	
net_connect = CH(**cisco)
net_connect.find_prompt()
net_connect.send_command("enable")
net_connect.find_prompt()
net_connect.send_command("configure terminal")
net_connect.find_prompt()
net_connect.send_command("hostname R1") #Hostname
net_connect.find_prompt()
net_connect.send_command("enable secret cisco") 
net_connect.find_prompt()
net_connect.send_command("banner motd #Todo acceso no autorizado esta estrictamente prohibido y sera perseguido por la ley! #")
net_connect.find_prompt()
net_connect.send_command("line console 0\nexec-timeout 15  \npassword cisco\n login\nlogging sync \nexit") 
net_connect.find_prompt()
net_connect.send_command("line vty 0 15\n exec-timeout 15 \npassword cisco\n login\nlogging sync \n transport input ssh \n login local \n exit") #VTY
net_connect.find_prompt()
net_connect.send_command("crypto key generate rsa\n 1024\n ip domain-name cisco.com\n ip ssh version 2 \n service password-enc \n username rodrigo secret cisco") #SSH
net_connect.find_prompt()
print(net_connect.send_command("do show running"))

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