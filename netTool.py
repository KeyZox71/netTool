from requests import *
import socket
import os
import re
import subprocess
from scapy.all import *
import random
import time

print('[+] Choice :')
print('1 - Scan Network')
print('2 - Scan port')

choice = int(input('Type your choice : '))

if choice == 1:

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

if choice == 3:
	site = input("Website IP : ")
	user = input("HTML user code : ")
	passwd = input("HTML password code : ")
	username = input("Username : ")
	password_list = input("Password list name : ")
	bad_pswd = input("Type bad password message : ")
	good_pswd = input("Type good password message : ")

	with open(password_list) as f:
		content = f.readline()
	for password in content:
		password = password.rstip()
		payload = {user: username , passwd: password}
		print('[*] Testing : ' + password)
		res = post(site,data=payload).content(bad_pswd, res.decode('utf-8'))
		if find is None:
			print("Password find : " + password)
			break