#!/usr/bin/python3
from scapy.all import *
import sys


sniff(iface=sys.argv[1], count=100, filter=sys.argv[2], prn=lambda x: x.summary())
