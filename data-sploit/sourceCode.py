from termcolor import *
import requests

banner = """
█▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ █░░█ 
█▄▄▀ █░░█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀ █▄▄█ 
▀░▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀░ ▀▀▀ ▀░▀▀ ▄▄▄█

░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝
"""
title ="[+] Download Website Source Code [+]"

print (colored(banner, "green"))
print (colored(title, "yellow"))
url = input(colored("example http://google.com: \n","cyan"))
fileName = input(colored("file name?","cyan"))
if len(url) == 0 and len(fileName) ==0:
	print (colored("[-_-] sorry data is empty","red"))
else:
	request = requests.get(url).text
	with open(fileName + ".html", "a") as file :
		print (colored("[+].........wait........[+]","cyan"))
		print (request,file = file)
		print (colored("done","cyan"))


