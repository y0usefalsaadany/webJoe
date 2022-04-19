from termcolor import *
import sys
import requests		

banner = """


███████╗░█████╗░██╗░░░░░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔══██╗
█████╗░░██║░░██║██║░░░░░██║░░██║█████╗░░██████╔╝
██╔══╝░░██║░░██║██║░░░░░██║░░██║██╔══╝░░██╔══██╗
██║░░░░░╚█████╔╝███████╗██████╔╝███████╗██║░░██║
╚═╝░░░░░░╚════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝

██████╗░░█████╗░████████╗██╗░░██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██║░░██║██╔════╝
██████╔╝███████║░░░██║░░░███████║╚█████╗░
██╔═══╝░██╔══██║░░░██║░░░██╔══██║░╚═══██╗
██║░░░░░██║░░██║░░░██║░░░██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
"""
print (colored(banner,"red"))
url = input(colored("Enter example 'http://www.google.com' :\n","yellow"))
file = open("data-sploit/paths.txt","r")
read_list = file.read()
paths = read_list.splitlines()
file_name = input(colored("enter name text file : ","yellow"))
if url == "" or file_name =="":
	print (colored("[-_-] sorry enter info correct","red"))
elif not "http" in url:
	print (colored("[-_-] sorry enter url with http","red"))
else:
	print (colored("-" * 40 ,"green"))
	print (colored("[+]...............wait...............[+]","green"))
	print (colored("-" * 40 ,"green"))
	for word in paths:
		words = f"{url}/{word}"
		try:
			request = requests.get(words ,"html.parser")
			if request.status_code == 200:
				print (colored(f"[+] link -->: {words} ", "red"))
			
				with open(f"data-sploit/files/{file_name}.txt","a") as list :
					print(words, file = list)
		except requests.ConnectionError:
			pass
		except KeyboardInterrupt:
			print (colored("-" * 40 ,"green"))
			print (colored("[+]...............Done...............[+]","green"))
			print (colored("-" * 40 ,"green"))
			sys.exit()
			
