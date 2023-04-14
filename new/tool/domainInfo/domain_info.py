import whois
from termcolor import *

def check_domain(domain):
    if len(domain) ==0 :
        print (colored("[-_-] sorry data is empty","red"))
    else:
        loading('Wait')
        if get_info(domain):
            whois_info = whois.whois(this.domain)
        loading('Done')

def get_info(domain):
    info = whois.whois(domain)
    print (colored(info,"green"))

def loading(msg):
    print (colored(f"-" * 48 ,"yellow"))
    print (colored(f"[+]	 	 ....{ msg }.... 		 ","yellow"))
    print (colored(f"-" * 48 ,"yellow"))

domain = str(input("Enter Domain Name : "))
check_domain(domain)