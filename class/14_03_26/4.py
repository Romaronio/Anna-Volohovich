import ipaddress
from ipaddress import *
k=0
net = ip_network('252.32.33.87/16', 0)
for ip in net:
    if bin(int(ip))[2:18].count('1') < ((bin(int(ip))[18:].count('1'))/2):
        k+=1
print(k)
