#!/usr/bin/python
#using typical attributes
import sys
from os import system
if(len(sys.argv)) < 3:
    print("\nUsage: " + sys.argv[0] + " [host name] [tap number] [optional: number of cores(1)] [optional: memory size(4G)]\n")
    sys.exit()
if(len(sys.argv)) >= 3:
    num_cores = sys.argv[3]
else:
    num_cores = '1'
if(len(sys.argv)) == 4:
    memory_size = sys.argv[4]
else:
    memory_size = '4'
filename = sys.argv[1]
tap_no = sys.argv[2]
system("qemu-system-x86_64 -enable-kvm -drive file=" + filename + ",format=qcow2 -net nic,macaddr='52:54:00:12:34:5'" + tap_no + ",model=virtio -net tap,ifname=tap" + \
tap_no + ",script=no,downscript=no,vhost=on -vga std -usbdevice tablet -machine type=pc,accel=kvm -smp " + num_cores + \
" -m " + memory_size + "G -cpu host &")
