#!/usr/bin/python3
from scapy.all import *
import sys

# Run example: sudo python3 filter.py [filters (only icmp or tcp)]
# Run example: sudo filter.py ens33 icmp
filters = sys.argv[1]

if(str(filters) == 'icmp'):
    sniff(count=5, filter=str(
        filters), prn=lambda x: x.summary())

elif(filters == 'tcp'):
    port = input("enter a port number to listen...\n")
    tcp_filter = 'tcp and port ' + str(port)
    sniff(count=5, filter=tcp_filter, prn=lambda x: x.summary())
else:
    raise Exception("for filters, please choose icmp or tcp")
