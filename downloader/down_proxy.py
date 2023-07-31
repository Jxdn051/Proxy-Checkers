import requests
import json
import time
import sys

def DownloadProxies(proxy_ver, out_file):
  with open("./list_proxy/proxy.json") as f:
    proxy_data = json.load(f)
  
  if proxy_ver.upper() == "ALL":
    f = open(out_file,'wb')
    for api in proxy_data['socks4'] and proxy_data['socks5'] and proxy_data['http']:
      try:
        r = requests.get(api,timeout=5)
        f.write(r.content)
      except:
       pass
    f.close()
    try:#credit to All3xJ
      r = requests.get("https://www.socks-proxy.net/",timeout=5)
      part = str(r.content)
      part = part.split("<tbody‣")
      part = part[1].split("</tbody‣")
      part = part[0].split("<tr‣<td‣")
      proxies = ""
      for proxy in part:
        proxy = proxy.split("</td‣<td‣")
        try:
          proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
        except:
         pass
        fd = open(out_file,"a")
        fd.write(proxies)
        fd.close()
    except:
     pass
  
  if proxy_ver == "4":
    f = open(out_file,'wb')
    for api in proxy_data['socks4']:
      try:
        r = requests.get(api,timeout=5)
        f.write(r.content)
      except:
       pass
    f.close()
    try:#credit to All3xJ
      r = requests.get("https://www.socks-proxy.net/",timeout=5)
      part = str(r.content)
      part = part.split("<tbody‣")
      part = part[1].split("</tbody‣")
      part = part[0].split("<tr‣<td‣")
      proxies = ""
      for proxy in part:
        proxy = proxy.split("</td‣<td‣")
        try:
          proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
        except:
         pass
        fd = open(out_file,"a")
        fd.write(proxies)
        fd.close()
    except:
     pass
    
  if proxy_ver == "5":
    f = open(out_file,'wb')
    for api in proxy_data['socks5']:
      try:
        r = requests.get(api,timeout=5)
        f.write(r.content)
      except:
       pass
    f.close()
  
  if proxy_ver == "http":
    f = open(out_file,'wb')
    for api in proxy_data['http']:
      try:
        r = requests.get(api,timeout=5)
        f.write(r.content)
      except:
       pass
    f.close()

  print("\r\n‣ Have already downloaded proxies list as "+out_file)