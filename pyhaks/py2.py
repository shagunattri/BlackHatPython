import nmap 
ns = nmap.PortScanner()
print(ns.nmap_version())
ns.scan('192.168.0.1','22-445','-v --version-all')
print(ns.scaninfo())

print(ns.csv())

print(ns.scanstats())

print(ns.all_hosts())

print(ns['192.168.0.1'].state())

print(ns['192.168.0.1'].all_protocols())  #all protocols running and open

print(ns["192.168.0.1"].["tcp"].keys()) #open ports

print(ns['192.160.0.1'].has_tcp(80))

