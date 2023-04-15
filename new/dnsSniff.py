from scapy.all import *
from termcolor import*
inpt = input("interface name : ")
print (colored(inpt, "yellow"))

def packet(pkt):
	if pkt.haslayer(DNS):
		if pkt.haslayer(DNSQR) and pkt.haslayer(IP):
			dns ="dns " + str(pkt.getlayer(DNS).qname) + " [+] from ip : " + str(pkt.getlayer(IP).src) +" [+]"
			print(dns)

sniff(iface=inpt, store=0, prn=packet)
