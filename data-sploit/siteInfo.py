import os
from termcolor import *
import socket
chooses = """
1- Know the website ip address 
2- Know the site domain info
"""
banner = """

█▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█
█▄▀ █▄█ █░▀░█ █▀█ █ █░▀█

██╗███╗░░██╗███████╗░█████╗░
██║████╗░██║██╔════╝██╔══██╗
██║██╔██╗██║█████╗░░██║░░██║
██║██║╚████║██╔══╝░░██║░░██║
██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
"""
print (colored(banner, "blue"))
print (" [+] website collector [+]")
print (colored(chooses,"green"))
msg = "Please Choose Number "
inpt = input("choose number => ")

if inpt == "1":
	domain = input("Enter Domain Name : ")
	getIp = socket.gethostbyname(domain)
	os.system('cls ||clear')
	print (getIp)

elif inpt == "2":
	os.system('cls ||clear')
	import domain_info
	
else:
	print (colored("[-_-] sorry enter info correct","red"))

