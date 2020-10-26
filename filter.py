#!/usr/bin/python3
from scapy.all import *
import sys

# Run example: sudo filter.py [your_interface], [filters (only icmp or tcp)]
# Run example: sudo filter.py ens33 icmp

interface = sys.argv[1]
filters = sys.argv[2]

sniff(iface=str(interface), count=5, filter=str(
    filters), prn=lambda x: x.summary())
