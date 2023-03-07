from bs4 import BeautifulSoup
from termcolor import *
import requests
class sourceCode:
    def __init__(this):
        this.banner()
        this.download_source_code()

    def banner(this):
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

    def download_source_code(this):
        url = input(colored("example http://google.com: \n","cyan"))
        fileName = input(colored("file name?","cyan"))
        if len(url) == 0 and len(fileName) ==0:
            print (colored("[-_-] sorry data is empty","red"))
        else:
            request = requests.get(url).content
            import urllib.request
            # request = urllib.request.urlopen(url)
            # soup = BeautifulSoup( request , 'html.parser')
            with open(fileName + ".html", "a") as file :
                print (colored("[+].........wait........[+]","cyan"))
                print (request,file = file)
                print (colored("done","cyan"))



