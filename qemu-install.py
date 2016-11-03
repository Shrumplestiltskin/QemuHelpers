#!/usr/bin/python
#installer wrapper, add disk image name, file, and tap number
import sys
from os import system
if(len(sys.argv)) < 4:
    print("\nUsage: " + sys.argv[0] + " [host name] [iso name] [tap number] [optional: number of cores(1)] [optional: memory size(4G)]\n")
    sys.exit()
if(len(sys.argv)) >= 4:
    num_cores = sys.argv[4]
else:
    num_cores = '1'
if(len(sys.argv)) == 5:
    memory_size = sys.argv[5]
else:
    memory_size = '4'
filename = sys.argv[1]
imagename = sys.argv[2]
tap_no = sys.argv[3]
system("qemu-system-x86_64 -enable-kvm -cdrom " + imagename + " -boot order=d -drive file=" + filename + ",format=qcow2 -net\
 nic,macaddr='52:54:00:12:34:5'" + tap_no + ",model=virtio -net tap,ifname=tap" + tap_no + ",script=no,downscript=no,vhost=on -vga std -usbdevice tablet\
 -machine type=pc,accel=kvm -smp " + num_cores + " -m " + memory_size + "G -cpu host &")
