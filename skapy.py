#!/usr/bin/python3
from scapy.all import *
import sys

filters = sys.argv[1]
sniff(iface='ens33', count=5, filter=str(filters), prn=lambda x: x.summary())
