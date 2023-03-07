import socket
from termcolor import *
banner = """

██████╗░░█████╗░██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░


░██████╗░█████╗░░█████╗░███╗░░██╗
██╔════╝██╔══██╗██╔══██╗████╗░██║
╚█████╗░██║░░╚═╝███████║██╔██╗██║
░╚═══██╗██║░░██╗██╔══██║██║╚████║
██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
"""
print (colored(banner, "green"))
ip = input("Enter Ip : ")


def check_port():
	def scan(port):
		ipv4 = socket.socket(socket.AF_INET)
		try:
			ipv4.connect((ip,port))
		except:
			return False
		else:
			return True
		
	for port in range(1025):
		if scan(port):
			print (colored(f"| this port {port}  	 	:   	 open  |","green"))
		#else:
			#print (colored(f"| this port {port}  	 	:   	 close |","red"))

###########port########
	
if ip == "":
	print (colored("[-_-] sorry enter info correct","red"))
else:
	print (colored(f"-" * 48 ,"yellow"))
	print (colored(f"[+]	 	 ....Wait.... 		 ","yellow"))
	print (colored(f"-" * 48 ,"yellow"))
	check_port()
	print (colored(f"-" * 48 ,"yellow"))
	print (colored(f"[+]	 	 ....Done.... 		 ","yellow"))
	print (colored(f"-" * 48 ,"yellow"))
	import network
