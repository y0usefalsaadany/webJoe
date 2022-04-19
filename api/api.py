import os
from termcolor import *
import sys
from termcolor import *
import requests

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

def api():
    url = input(colored("Enter example 'http://www.google.com/api' :\n","yellow"))
    file = open("api/without-api.txt","r")
    read_list = file.read()
    apis = read_list.splitlines()
    if url == "":
        print (colored("[-_-] sorry enter info correct","red"))
    elif not "http" in url:
        print (colored("[-_-] sorry enter url with http or /api/ or api/","red"))
    else:
        print (colored("-" * 40 ,"green"))
        print (colored("[+]...............wait...............[+]","green"))
        print (colored("-" * 40 ,"green"))
        for word in apis:
            words = f"{url}/{word}"
            try:
                request_get = requests.get(words ,"html.parser")
                if request_get.status_code == 200:
                    print (colored(f"[+] Get Method : link -->: {words} ", "yellow"))
                
                    with open("api/output.txt","a") as list :
                        print(words, file = list)
                
                request_post = requests.post(words ,"html.parser")
                if request_post.status_code == 200:
                    print (colored(f"[+] Post Method :link -->: {words} ", "yellow"))
                
                    with open("api/output.txt","a") as list :
                        print(words, file = list)

                request_put = requests.put(words ,"html.parser")
                if request_put.status_code == 200:
                    print (colored(f"[+] Put Method :link -->: {words} ", "yellow"))
                
                    with open("api/output.txt","a") as list :
                        print(words, file = list)
                
                request_delete = requests.delete(words)
                if request_delete.status_code == 200:
                    print (colored(f"[+] Delete Method :link -->: {words} ", "yellow"))
                
                    with open("api/output.txt","a") as list :
                        print(words, file = list)

            except requests.ConnectionError:
                print (colored(f"[+]Not found", "green"))
                pass
            except KeyboardInterrupt:
                print (colored("-" * 40 ,"green"))
                print (colored("[+]...............Done...............[+]","green"))
                print (colored("-" * 40 ,"green"))
                sys.exit()
	
def without_api():
    url = input(colored("Enter example 'http://www.google.com/' :\n","yellow"))
    file = open("api/Api.txt","r")
    read_list = file.read()
    apis = read_list.splitlines()
    if url == "" or "/api/" in url or "api/" in url:
        print (colored("[-_-] sorry enter info correct","red"))
    elif not "http" in url:
        print (colored("[-_-] sorry enter url with http","red"))
    else:
        print (colored("-" * 40 ,"green"))
        print (colored("[+]...............wait...............[+]","green"))
        print (colored("-" * 40 ,"green"))
        for word in apis:
            words = f"{url}/{word}"
            try:
                print(f"{url}/{word}")
                request = requests.get(words ,"html.parser")
                if request.status_code == 200:
                    print (colored(f"[+] link -->: {words} ", "yellow"))
                
                    with open("api/output.txt","a") as list :
                        print(words, file = list)
            except requests.ConnectionError:
                pass
            except KeyboardInterrupt:
                print (colored("-" * 40 ,"green"))
                print (colored("[+]...............Done...............[+]","green"))
                print (colored("-" * 40 ,"green"))
                sys.exit()
			


try:
    banner2 = """
    1- collector with api in link
    2- collector without api in link
    """
    print(banner2)
    start = int(input('Choose number : \n'))
    if start == 1:
        api()
    if start == 2:
        without_api()
    else:
        print('enter correct number')
except KeyboardInterrupt:
    sys.exit()