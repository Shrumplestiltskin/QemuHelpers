#!/usr/bin/python
from os import system
import sys
if len(sys.argv) < 3:
    print("\nUsage: " + sys.argv[0] + " [name of file] [file size in GB]\n")
    sys.exit()
filesize = sys.argv[2]
filename = sys.argv[1]
system("qemu-img create -f qcow2 " + filename + " " + filesize + "G")
