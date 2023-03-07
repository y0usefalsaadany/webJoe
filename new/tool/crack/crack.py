import hashlib
import os
import sys
from termcolor import *
from termcolor import *

def crack(open_list):
	hash_text = input("Enter hash password : \n")
	for password in open_list:
		enc_pass = password.encode("utf-8")
		if len(hash_text) == 32:
			hash_password = hashlib.md5(enc_pass.strip()).hexdigest()
		if len(hash_text) == 40:
			hash_password = hashlib.sha1(enc_pass.strip()).hexdigest()
		# print (hash_password)
		if hash_password == hash_text:
			print('password is : ' + colored(password,"blue"))
			quit()
	print ("password not found\n")



os.system('cls||clear')
banner = """

░██╗░░░░░░░██╗███████╗██████╗░░░░░░██╗░█████╗░███████╗
░██║░░██╗░░██║██╔════╝██╔══██╗░░░░░██║██╔══██╗██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝░░░░░██║██║░░██║█████╗░░
░░████╔═████║░██╔══╝░░██╔══██╗██╗░░██║██║░░██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝┛
"""
print (colored(banner,"green"))
# hash_text = input("Enter hash password : \n")
try:
	open_list = open('./pas.txt',"r")
except KeyboardInterrupt:
	print("this list not found \n")
	sys.exit()

try:
    crack(open_list)
except:
    quit()
