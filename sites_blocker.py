import json
import time
from datetime import datetime as dt

raw = open('forbidden_wbs.json','r')
raw_cnt=raw.read()
host_path = input('Input your host path: ')
redirect = "127.0.0.1"

wb_list = json.loads(raw_cnt)
print(wb_list)
while True:
    
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
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
