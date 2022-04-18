import hashlib
import os
from termcolor import *
from termcolor import *

def md5(open_list):
	for password in open_list:
		enc_pass = password.encode("utf-8")
		hash_password = hashlib.md5(enc_pass.strip()).hexdigest()

		if hash_password == hash_text:
			print('password is : ' + password)
			quit()
	print ("password not found\n")

def sha1(open_list):
	for password in open_list:
		enc_pass = password.encode("utf-8")
		hash_password = hashlib.sha1(enc_pass.strip()).hexdigest()

		if hash_password == hash_text:
			print('password is : ' + password)
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
hash_text = input("Enter hash password : \n")
guess_list = input("Enter name password list : \n")
try:
	open_list = open(guess_list,"r")
except:
	print("this list not found \n")
	quit()

try:
    banner = """
    1- sha1
    2- md5
    """
    print(banner)
    start = int(input('Choose number : \n'))
    if start == 1:
        sha1(open_list)
    if start == 2:
        md5(open_list)
    else:
        print('enter correct number')
except:
    quit()
