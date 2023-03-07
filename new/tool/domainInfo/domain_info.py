import whois
from termcolor import *

class domain_info:
    domain =''
    def __init__(this):
        this.domain = str(input("Enter Domain Name : "))
        this.check_domain()

    def check_domain(this):
        if len(this.domain) ==0 :
            print (colored("[-_-] sorry data is empty","red"))
        else:
            this.loading('Wait')
            
            if this.get_info():
                whois_info = whois.whois(this.domain)

            this.loading('Done')

    def get_info(this):
        info = whois.whois(this.domain)
        print (colored(info,"green"))

    def loading(this,msg):
            print (colored(f"-" * 48 ,"yellow"))
            print (colored(f"[+]	 	 ....{ msg }.... 		 ","yellow"))
            print (colored(f"-" * 48 ,"yellow"))
