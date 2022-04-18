from termcolor import *
import requests
import sys				

banner = """

█▀ █░█ █▄▄ █▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█
▄█ █▄█ █▄█ █▄▀ █▄█ █░▀░█ █▀█ █ █░▀█

█▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
█▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄▄ ░█░ █▄█ █▀▄
"""
print (colored(banner,"green"))
url = input(colored("Enter url  without www example 'google.com' :\n","yellow"))
if url == "":
	print (colored("[-_-] sorry enter info correct","red"))
else:
	if "http" in url or "www" in url:
		print (colored("[-_-] sorry enter url without http or www","red"))
	else:
		file = open("subdomain.txt","r")
		read_list = file.read()
		subdomains = read_list.splitlines()
		file_name = input(colored("enter name text file : ","yellow"))
		print (colored("-" * 40 ,"green"))
		print (colored("[+]...............wait...............[+]","green"))
		print (colored("-" * 40 ,"green"))
		for sub in subdomains:
			domain = f"http://{sub}.{url}"
			try:
				request = requests.get(domain ,"html.parser")
				if request.status_code == 200:
					print (colored(f"[+] subdomain: {domain} ","cyan"))
			
					with open(f"{file_name}.txt","a") as list :
						print(domain, file = list)
			except requests.ConnectionError:
				pass
			except KeyboardInterrupt:
				print (colored("-" * 40 ,"green"))
				print (colored("[+]...............Done...............[+]","green"))
				print (colored("-" * 40 ,"green"))
				sys.exit()
			