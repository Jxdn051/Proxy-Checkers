#!/usr/bin/python3
#Coded by L330n123
#Remake By Jxdn
import os, sys
import time
from downloader.down_proxy import DownloadProxies
from scanning.proxy_scan import check_socks, check_list

print("@Remake by Jxdn\n[!] Downloader Proxy And Scanning")

def help():
  print("""
━━━━━━━━━━━━━━━━━━━━ Help ━━━━━━━━━━━━━━━━━━━━
     down          | Proxy Type is (4/5/http)
                   | To download fresh proxy 
                   | with you use this command.
     scan          | This function is to scan
                   | proxies or filter proxies 
                   | that are turned off or on 
                   | will be filtered.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  """)

def loading():
    for _ in range(30):
        sys.stdout.write("\r‣ Downloading proxies [-]")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r‣ Downloading proxies [/]")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r‣ Downloading proxies [|]")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r‣ Downloading proxies [\\]")
        sys.stdout.flush()
        time.sleep(0.1)

def end_loading(result):
    sys.stdout.write("\r" + result)
    sys.stdout.flush()

if len(sys.argv) < 4:
    print("Usage: python proxy.py [down/scan] [4/5/http] [file_name]")
    sys.exit(1)

args = sys.argv[1].lower()
proxy_ver = sys.argv[2]
out_file = sys.argv[3]

if args == "down":
    loading()
    DownloadProxies(proxy_ver, out_file)
    check_list(out_file)
    with open(out_file, 'r') as f:
        proxies = f.readlines()
    result = f"\r\n‣ Number Of Proxies: {len(proxies)}"
    end_loading(result)
elif args == "scan":
    check_socks(proxy_ver,out_file, 3)
elif args == "help":
    help()
else:
    print("Usage: python proxy.py [down/scan/help] [4/5/http] [file_name]")
