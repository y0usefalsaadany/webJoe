import random , os
from termcolor import *
import sys
from termcolor import *
import requests
import socket

## COLORS ###############
wi="\033[1;37m" 
rd="\033[1;31m" 
gr="\033[1;32m" 
yl="\033[1;33m" 
#########################

os.system('cls||clear')
banner = """
          Joe framwork tool for penetesters and devolpoers

░██╗░░░░░░░██╗███████╗██████╗░░░░░░██╗░█████╗░███████╗
░██║░░██╗░░██║██╔════╝██╔══██╗░░░░░██║██╔══██╗██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝░░░░░██║██║░░██║█████╗░░
░░████╔═████║░██╔══╝░░██╔══██╗██╗░░██║██║░░██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝┛
----------------------------------------------------
Facebook : https://www.facebook.com/Yousef.Elsa3dany
Github   : https://github.com/y0usefalsaadany
----------------------------------------------------
"""
print (colored(banner,"green"))

chooises = f"""
{rd}[{yl}1{rd}]  Domain information
[{yl}2{rd}]  Download source code
[{yl}3{rd}]  Subdomain collector
[{yl}4{rd}]  Website paths collector
[{yl}5{rd}]  Api paths collector
[{yl}6{rd}]  Make list for brute force
[{yl}7{rd}]  Crack hash(md5,sha1)

----------------------------------------------------
"""
while True:
	try:
		print(chooises)
		inpt = input("Choose Number : ")
		sys.path.insert(0, 'data-sploit')
		if inpt == "1":
			import siteInfo

		if inpt == "2":
			import sourceCode
			
		if inpt == "3":
			import subdomain
			
		if inpt == "4":
			import paths
		sys.path.insert(0, 'api')
		if inpt == "5":
			import api

		sys.path.insert(0, 'make_list')
		if inpt == "6":
			import list
		
		sys.path.insert(0, 'crack')
		if inpt == "7":
			import crack
			
		else:
			print ('Enter one of the numbers shown in front of you.')
	except KeyboardInterrupt:
		sys.exit()
