from ipaddress import *
k=0
net= ip_network('146.180.173.153/255.192.0.0',0)
for ip in net:
    k+=1
print(k, ip)