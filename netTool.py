from requests import *
import socket
import os
import re
import subprocess
from scapy import *
import random
import time

print('[+] Choice :')
print('1 - Scan Network')
print('2 - Scan port')
print('---------------')
print('99 - Exit')

choice = int(input('Type your choice : '))

if choice == 1:
	print('[+] Choice :')
	print('1 - Scan 255.255.255.X')
	print('2 - Scan 255.255.X.X')
	print('3 - Scan 255.X.X.X')
	print('4 - Scan X.X.X.X')
	print('---------------')
	print('99 - Exit')
	choiceScNet = int(input('Type your choice : '))

	if choiceScNet == 1:
		hosts = []
		ip = input('Type your ip type (exemple : 192.168.1.) : ')
		x = 0
		stop = int(input('Max ip scan : '))

		while x<=stop:
			p = subprocess.Popen('ping ' + ip + str(x) + " -n 1", stdout=subprocess.PIPE, shell=True)
			out, error = p.communicate()
			out = str(out)
			find = re.search("Impossible de joindre", out)
			if find is None:
				hosts.append(ip + str(x))
				print("[Info] Host found")
			x = x + 1
		print("--------------------------")
		print("-----      Host      -----")
		for host in hosts:
			try:
				name, a, b = socket.gethostbyaddr(host)
			except:	
				name = "Not found"
			print(host + " : " + name)
	if choiceScNet == 2:
		exit()
	if choiceScNet == 3:
		exit()
	if choiceScNet == 4:
		exit()
	if choiceScNet == 99:
		exit()
if choice == 2:
	port_to_scan = [21,22,80,25565,8080,443]
	open_ports = []
	ip = input("Ip to scan : ")
	ip_usr = input("Your ip : ")

	for port in port_to_scan:
		p = IP(dst=ip, src=ip_usr)/TCP(dport=port, sport=random.randint(0, 1024), flags="S")
		r = srl(p)
		time.sleep(2)
		if r['TCP'].flags == 18:
			open_ports.append(port)
			p = IP(dst=ip, src=ip_usr)/TCP(dport=port, sport=random.randint(0, 1024), flags="AR")
			send(p)
	for port in open_ports:
		print(str(port + " ---- OPEN"))	

if choice == 99:
	exit()