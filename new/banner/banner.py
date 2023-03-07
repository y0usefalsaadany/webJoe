import os
from termcolor import *
import sys

class banner:

    def __init__(this):
        (this.title())
        (this.choices())
    def title(this):

        os.system('cls||clear')
        description ="""
        Joe framework tool for penetesters and develpoers
        """
        banner = f"""
        ░██╗░░░░░░░██╗███████╗██████╗░░░░░░██╗░█████╗░███████╗
        ░██║░░██╗░░██║██╔════╝██╔══██╗░░░░░██║██╔══██╗██╔════╝
        ░╚██╗████╗██╔╝█████╗░░██████╦╝░░░░░██║██║░░██║█████╗░░
        ░░████╔═████║░██╔══╝░░██╔══██╗██╗░░██║██║░░██║██╔══╝░░
        ░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝╚█████╔╝███████╗
        ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝┛
        """
        contact = """
        ----------------------------------------------------
        Facebook : https://www.facebook.com/Yousef.Elsa3dany
        Github   : https://github.com/y0usefalsaadany
        ----------------------------------------------------
        """
        print (colored(description,"green"))
        print (colored(banner,"red"))
        print (colored(contact,"yellow"))

    def choices(this):

        choices = f"""
        1-  Domain information
        2-  Download source code
        3-  Subdomain collector
        4-  Website paths collector
        5-  Api paths collector
        6-  Make list for brute force
        7-  Crack hash(md5,sha1)
        8-  Port scanning

        ----------------------------------------------------
        """
        print (colored(choices,"cyan"))




