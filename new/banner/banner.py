import os
from termcolor import *
import sys
from termcolor import *

class banner:

    def __init__(this):
        print (this.title())
        print (this.choices())
    def title(this):

        os.system('cls||clear')
        banner = """
        Joe framework tool for penetesters and develpoers

        ░██╗░░░░░░░██╗███████╗██████╗░░░░░░██╗░█████╗░███████╗
        ░██║░░██╗░░██║██╔════╝██╔══██╗░░░░░██║██╔══██╗██╔════╝
        ░╚██╗████╗██╔╝█████╗░░██████╦╝░░░░░██║██║░░██║█████╗░░
        ░░████╔═████║░██╔══╝░░██╔══██╗██╗░░██║██║░░██║██╔══╝░░
        ░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝╚█████╔╝███████╗
        ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝┛
        ----------------------------------------------------
        Facebook : https://www.facebook.com/Yousef.Elsa3dany
        Github   : https://github.com/y0usefalsaadany
        ----------------------------------------------------
        """
        return (colored(banner,"green"))

    def choices(this):
        wi="\033[1;37m"
        rd="\033[1;31m"
        gr="\033[1;32m"
        yl="\033[1;33m"
        choices = f"""
        {rd}[{yl}1{rd}]  Domain information
        [{yl}2{rd}]  Download source code
        [{yl}3{rd}]  Subdomain collector
        [{yl}4{rd}]  Website paths collector
        [{yl}5{rd}]  Api paths collector
        [{yl}6{rd}]  Make list for brute force
        [{yl}7{rd}]  Crack hash(md5,sha1)

        ----------------------------------------------------
        """
        return choices





