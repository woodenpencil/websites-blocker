#Import libraries
import time
from datetime import datetime as dt

#Path to the host file, redirect to local host, list of websits to block
host_path = "D:\\newfolder\\py_projects\\hosts"
redirect = "127.0.0.1"
wb_list = ["www.netflix.com","www.facebook.com"]

#Condition
while True:
    #Check for the current time
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Rihanna")
        hosts=open(host_path,'r+')
        content=hosts.read()
        for wb in wb_list:
        	if wb not in content:
        		hosts.write(redirect+' '+wb+'\n')
    else:
        print("Drake")
        hosts=open(host_path,'r+')
        content=hosts.readlines()
        hosts.seek(0)
        for line in content:
        	if not any((wb_ in line)for wb_ in wb_list):
        		hosts.write(line)
        hosts.truncate()
    time.sleep(5)
