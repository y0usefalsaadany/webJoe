import random , os
from termcolor import *
import sys , socket
import whois
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
print (colored(banner, "yellow"))
print (" [+] website collector [+]")
print (colored(chooses,"green"))
msg = "Please Choose Number "
inpt = input("choose number => ")

if inpt == "1":
	domain = input("Enter Domain Name : ")
	getIp = socket.gethostbyname(domain)
	print (getIp)

elif inpt == "2":
	import domain_info
	
else:
	print (colored("[-_-] sorry enter info correct","red"))

