import sys
sys.path.insert(0,'../banner')
sys.path.insert(0,'../choices')
from banner import banner
from choices import choices

banner = banner.banner()

inpt = input("Choose Number : ")
try:
    choose = choices.choices(int(inpt)).tool()
except ValueError:
    print("The input must be an integer")
