#!/usr/bin/python2
# coding=utf-8
# Author: IqbalDev
# Tool Instaram
# Versi 0.5

a = "\033[96;1m"
p = "\033[97;1m"
h = "\033[92;1m"
k = "\033[93;1m"
m = "\033[91;1m"
d = "\033[90;1m"

import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

try:
	from bs4 import BeautifulSoup
except ImportError:
	print k+"\n Modul Bs4 blom terinstall!..."
	os.system("pip install bs4" if os.name == "nt" else "pip2 install bs4")

import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time
from calendar import monthrange
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

garis = h+"+++>"

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
platform_dev = str(platform.platform()).lower()
list_proxy = []

try:
	has_ok = open("hasil_ok.txt", "r").readlines()
	with open("hasil_ok.txt", "w") as tul:
		tul.write("")
	for dev in set(has_ok):
		with open("hasil_ok.txt", "a") as tu:
			tu.write(dev)
except:
	pass
try:
	has_cp = open("hasil_cp.txt", "r").readlines()
	with open("hasil_cp.txt", "w") as tul:
		tul.write("")
	for dev in set(has_cp):
		with open("hasil_cp.txt", "a") as tu:
			tu.write(dev)
except:
	pass

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "ZGVmIGlxYmVsKGlxKToKCXRyeToKCQlzZW1fcGFrX2JvbF9vbmcgPSAiIgoJCWlxYmFsID0gaXEKCQlwYW56eiA9IHNlbV9wYWtfYm9sX29uZy5zcGxpdCgpCglleGNlcHQ6CgkJcGFzcwoJCQpkZWYgaXFiYWwoZGV2Xyk6CglnbG9iYWwgaQoJdHJ5OgoJCWlxYmFsX2Rldl8gPSAiIgoJCWRldiA9IGRldl8uc3BsaXQoIiUiKQoKCQlmb3IgaXFiYWxfIGluIGRldjoKCQkJdHJ5OgoJCQkJaXFiYWxfZGV2XyArPSBpcWJhbF9bMF0KCQkJZXhjZXB0OgoJCQkJcGFzcwoJCWkgPSBiYXNlNjQuYjY0ZGVjb2RlKGlxYmFsX2Rldl8pCgoJZXhjZXB0OgoJCXBhc3MKCg=="]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -rf cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -rf cokiz.txt")
	except:
		pass

def cek_hasil():
	print garis
	print h+" >"+k+" 1"+p+". Cek Hasil "+h+"OK/Live"
	print h+" >"+k+" 2"+p+". Cek Hasil "+k+"Checkpoint"
	print h+" >"+k+" 3"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"+p+"/"+h+"Live"
	print garis
	while True:
		pil = raw_input(a+" ? "+p+"Pilih"+h+": ")
		if pil == "1":
			try:
				hasil_ok_ = open("hasil_ok.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+h+"Live\n"
				for dev in hasil_ok_:
					ok = dev.replace("\n", "").split("==>")
					print a+"  {"+k+"Live"+a+"} "+h+ok[1]+a+" | "+p+ok[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_ok_))
			except:
				print k+"\n Belum ada hasil"+h+" OK"
			break
		elif pil == "2":
			try:
				hasil_cp_ = open("hasil_cp.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+k+"Checkpoint\n"
				for dev in hasil_cp_:
					cp = dev.replace("\n", "").split("==>")
					print a+"  {"+p+"Chek"+a+"} "+k+cp[1]+a+" | "+d+cp[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_cp_))
			except:
				print k+"\n Belum ada hasil"+p+" CP"
			break
		elif pil == "3":
			print "   "+ garis
			print  h+"   >"+k+" 1"+m+". Hapus"+p+" Hasil "+k+"Live"
			print  h+"   >"+k+" 2"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"
			print "   "+ garis
			while True:
				pil_hps = raw_input(a+"   ? "+p+"Pilih"+h+": ")
				yakin = raw_input(a+"   ? "+p+"Yakin mau Hapus?"+h+" y/n: ")
				if pil_hps == "1" and yakin == "y":
					try:
						os.system("del hasil_ok.txt" if os.name == "nt" else "rm -rf hasil_ok.txt")
						print h+"\n    Sukses Hapus Hasil Live\n"
					except:
						print k+"\n    Belum ada Hasil Live\n"
					exit()
				elif pil_hps == "2" and yakin == "y":
					try:
						os.system("del hasil_cp.txt" if os.name == "nt" else "rm -rf hasil_cp.txt")
						print h+"\n    Sukses Hapus Hasil Checkpoint\n"
					except:
						print k+"\n    Belum ada Hasil Checkpoint\n"
					exit()
				elif yakin == "n":
					exit()
				else:
					pass
		else:
			pass

def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_dev()

	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print m+"\n Cookie Kedaluarsa...\n"
					hapus_cookie()
					login_dev()	
			except ValueError:
				print m+"\n Cookie Kedaluarsa...\n"
				hapus_cookie()
				login_dev()
			except requests.exceptions.ConnectionError:
				print m+"\n Tidak ada Koneksi Internet...\n"
				exit()

def login_dev_cookie():
	global cookie
	print "\n  Login Instagram\n"
	cok = raw_input(" Masukkan Cookie: ")
	with requests.Session() as ses_dev:
		login_coki = ses_dev.get(url_instagram, cookies={"cookie": cok}, headers=headerz)
		if "viewer_has_liked" in str(login_coki.content):
			print " Login Suksess...."
			with open("cookie.txt", "w") as tulis_coki:
				tulis_coki.write(cok)
			cookie = {"cookie": cok}
		else:
			print " Login gagal...."
			exit()

def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50

Lis_prox = []
c=1
def cek_proxy(proxy):
	try:
		respon = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=3).json()["origin"]
		print " >> Live -- "+proxy
		list_proxy.append(proxy)
		c+=1
	except:
		pass

def scrap():
	lis_prox_dev = []
	url="https://free-proxy-list.net/#list"
	with requests.Session() as ses_dev:
		respon = ses_dev.get(url)
		sop = BeautifulSoup(respon.content, "html.parser")
		tbody = sop.find("tbody")
		for dev in tbody.find_all("tr"):
			prox = dev.find_all("td", class_=False)
			lis_prox_dev.append(str(prox))
			print prox
		for dev in lis_prox_dev:
			pecah = dev.split(",")
			ip = pecah[0].replace("<td>", "").replace("</td>","").replace("[", "")
			port = pecah[1].replace("<td>", "").replace("</td>","").replace("[", "").strip(" ")
			lis_prox.append(ip+":"+port)

	with ThreadPoolExecutor(max_workers=20) as dev:
		for prox in lis_prox:
			dev.submit(cek_proxy, prox)

baner = """
.__  """+h+"""+{ I G E H }+"""+a+""" __        ______               
|  | ___   _______/  |_____  \____ \   ______  __
|  |/   \ /  ___/\   __\__ \  |  |  \_/ _ \  \/ /
|  |   | \\\___ \  |  |  / _ \_|  `   \  __/\   / 
|__|___| /____  > |__| (__  /_____  /\___  >\_/  
        /     \/          \/      \/     \/      
	"""
versi = k+" >_"+h+" Versi_:"+p+" 0.5\n"

if__name__=="__main__":
	cek_login()
	menu_dev()
