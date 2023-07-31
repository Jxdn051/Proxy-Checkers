import socks
import time
import threading
import sys,os
import socket

nums = 0
def checking(lines,proxy_type,ms,rlock,):#Proxy checker coded by Leeon123
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			if proxy_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if proxy_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if proxy_type == 0:
				s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect(("1.1.1.1", 80))
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(proxy_ver,out_file,ms):#Coded by Leeon123
	global nums
	global proxies
	proxies = open(out_file).readlines()
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		if proxy_ver == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if proxy_ver == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,rlock,))
			th.start()
		if proxy_ver == "http":
			th = threading.Thread(target=checking,args=(lines,0,ms,rlock,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("‣ Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("‣ Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\n‣ Checked all proxies, Total Worked:"+str(len(proxies)))
	
	with open(out_file, 'wb') as fp:
		for lines in list(proxies):
			fp.write(bytes(lines,encoding='utf8'))
		fp.close()
	print("‣ They are saved in "+out_file)

def check_list(socks_file):
    print("‣ Checked list and removed duplicates.")
    temp = open(socks_file).readlines()
    temp_list = []
    for i in temp:
        if i not in temp_list:
            if ':' in i and '#' not in i:
                try:
                    socket.inet_pton(socket.AF_INET, i.strip().split(":")[0])  # Check valid IPv4 address
                    temp_list.append(i)
                except:
                    pass
    with open(socks_file, "w") as rfile:
        for i in list(temp_list):
            rfile.write(i)