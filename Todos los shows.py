# Prueba basica de netmiko
# Programa para obtener las configuraciones

from netmiko import ConnectHandler as CH
R_zanahoria = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.105',
	'username': 'rodrigo',
	'password' : 'cisco'}
R_col = {
	'device_type': 'cisco_ios',
	'ip': '10.2.0.3',
	'username': 'rodrigo',
	'password' : 'cisco'}
R_apio = {
	'device_type': 'cisco_ios',
	'ip': '10.2.0.1',
	'username': 'rodrigo',
	'password' : 'cisco'}

R_cebolla = {
	'device_type': 'cisco_ios',
	'ip': '10.2.0.13',
	'username': 'rodrigo',
	'password' : 'cisco'}	

R_brocoli = {
	'device_type': 'cisco_ios',
	'ip': '10.2.0.14',
	'username': 'rodrigo',
	'password' : 'cisco'}	
S_tuna = {
	'device_type': 'cisco_ios',
	'ip': '10.2.0.18',
	'username': 'rodrigo',
	'password' : 'cisco'}
S_kiwi = {
	'device_type': 'cisco_ios',
	'ip': '',
	'username': 'rodrigo',
	'password' : 'cisco'}
S_pera = {
	'device_type': 'cisco_ios',
	'ip': '',
	'username': 'rodrigo',
	'password' : 'cisco'}
S_manzana = {
	'device_type': 'cisco_ios',
	'ip': '',
	'username': 'rodrigo',
	'password' : 'cisco'}
S_platano = {
	'device_type': 'cisco_ios',
	'ip': '',
	'username': 'rodrigo',
	'password' : 'cisco'}

devices = (R_zanahoria, R_col, R_apio, R_cebolla, R_brocoli, S_tuna,S_kiwi,S_pera,S_manzana, S_platano)
	
for device in devices:
	net_connect = CH(**device)
	net_connect.find_prompt()
	print(net_connect.send_command("show running"))


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