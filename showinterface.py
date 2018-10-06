import textfsm
from pprint import pprint
import netmiko
from getpass import getpass

ip = input("Insert IP: ")
username = input("Insert username: ")
password = getpass("Insert password: ")

cisco_vios = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': password,
}


net_connect = netmiko.ConnectHandler(**cisco_vios)

string_interface = net_connect.send_command('show interface')

template_file = open("showinterface.template")
template = textfsm.TextFSM(template_file)
result_template = template.ParseText(string_interface)

interface_list = list()
for list in result_template:
	resultDict = dict()
	resultDict["interface"] = list[0]
	resultDict["mac address"] = list[1]
	resultDict["ip address"] = list[2]
	resultDict["MTU"] = list[3]
	resultDict["bandwith"] = list[4]

	interface_list.append(resultDict)
pprint(interface_list)