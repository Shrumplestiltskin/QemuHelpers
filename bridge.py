#!/usr/bin/python
import sys
if(len(sys.argv)) < 3:
    print("\nUsage: " + sys.argv[0] + " [1-10] [main int]\nWhere 1-10 is tap\nnumber to be created\nand added to bridge\n\
main int is primary ethernet\nfor instance eth0\n")
    sys.exit()

from os import system
tap_no = sys.argv[1]
eth_no = sys.argv[2]
system("ip link add name br0 type bridge")
system("ip link set br0 up")
system("ip tuntap add dev tap" + tap_no + " mode tap")
system("ip link set tap" + tap_no + " up")
system("ip addr flush dev " + eth_no)
system("ip link set " +  eth_no + " master br0")
system("ip link set tap" + tap_no + " master br0")
system("systemctl restart dhcpcd")
