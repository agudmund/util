#!/usr/bin/env python

# Scans target for open ports.
# usage: ./port_scanner.py -z 213.213.128.4

import time
import random
import socket
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description='Port scanner')
parser.add_argument('-z', type=str,help='IP address to scan',action="store")
args = parser.parse_args()

THREADS = 512
CONNECTION_TIMEOUT = 1

def ping(host, port, results = None):
    try:
        socket.socket().connect((host, port))
        if results is not None:
            results.append(port)
        print(" Open\t%s"%str(port))
        return True
    except:
        return False

def scan_ports(host):
    available_ports = []
    socket.setdefaulttimeout(CONNECTION_TIMEOUT)
    with ThreadPoolExecutor(max_workers = THREADS) as executor:
        print("\nScanning ports on " + host + " ...")
        for port in range(1, 65535):
            executor.submit(ping, host, port, available_ports)
    print("\nDone.")
    available_ports.sort()
    print(str(len(available_ports)) + " ports available.")
    print(available_ports)

def reverse():
    for i in xrange(1,65535):
#        print 'Port %s' % i,

        if i in [21,22,25,443,445]: # exclude standard ports
 #           print "Skipping"
            continue

        result = requests.get("http://portquiz.net:%s" % i)
  #      print result.status_code,result.reason
        if not result.reason == "OK":
            break
        time.sleep(random.randint(1,5))

def main():
    scan_ports(args.z)
    
if __name__ == "__main__":
    main()
