#
# MUST RUN AS ADMIN / ROOT
#

import nmap3 # python3-nmap==1.6.0 
import pythonping
import os

PORT_MIN = 80
PORT_MAX = 443
TARGET = "103.27.227.191" # To be swapped out with target and cannot be a domain


def is_host_alive():
    return pythonping.ping(target=TARGET,count=5,timeout=5).success()

def scan_ports():
    # Using a SYN scan instead of TCP for speed
    return nmap3.NmapScanTechniques().nmap_syn_scan(target=TARGET,args="-p{min}-{max}".format(min=PORT_MIN,max=PORT_MAX))

def find_directories():
    os.system("urlbuster -W ./directory-list.txt https://" + TARGET)

if(is_host_alive()):
    mapper = scan_ports()
    print(mapper)

open_port_list = [] 

for entry in mapper[TARGET]["ports"]:
    # Function / Script injection if needed 
    port = entry["portid"]
    open_port_list.append(port)

print("\nTotal Ports: {list_size}".format(list_size=len(open_port_list)))
