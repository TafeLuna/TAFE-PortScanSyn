import nmap3 # python3-nmap==1.6.0 
TARGET = "192.168.0.135" # To be swapped out with target

mapper = nmap3.NmapScanTechniques().nmap_syn_scan(target=TARGET) # Using a SYN scan instead of TCP for speed

open_port_list = []

for entry in mapper[TARGET]["ports"]:
    # Function / Script injection if needed 
    port = entry["portid"]
    print(port)
    open_port_list.append(port)

print("\nTotal Ports: {list_size}".format(list_size=len(open_port_list)))