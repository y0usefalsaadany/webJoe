import requests , socket ,whois
from termcolor import *

def get_info(d):
		info = whois.whois(d)
		print (colored(info,"green"))
	
		

domain = input("Enter Domain Name : ")
if "http" in domain:
	print (colored("[-_-] sorry enter domain without http:// or https://","red"))
else:
	if len(domain) ==0 :
		print (colored("[-_-] sorry data is empty","red"))
	else:
		print (colored(f"-" * 48 ,"yellow"))
		print (colored(f"[+]	 	 ....Wait.... 		 ","yellow"))
		print (colored(f"-" * 48 ,"yellow"))
		
		if get_info(domain):
			whois_info = whois.whois(domain_name)
		
		print (colored(f"-" * 48 ,"yellow"))
		print (colored(f"[+]	 	 ....Done.... 		 ","yellow"))
		print (colored(f"-" * 48 ,"yellow"))

