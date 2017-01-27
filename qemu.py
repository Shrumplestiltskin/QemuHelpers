#!/usr/bin/python
import argparse
import sys
from os import system

qemu_img = "/usr/bin/qemu-img"
qemu_binary = "/usr/bin/qemu-system-x86_64 -enable-kvm "
qemu_tap_pre = " -net nic,macaddr='52:54:00:12:34:5'"
qemu_tap_mid = ",model=virtio -net tap,ifname=tap"
qemu_tap_post = ",script=no,downscript=no,vhost=on "
qemu_boiler = "-vga std -usbdevice tablet -machine type=pc,accel=kvm -smp "

def create(image, imagesize):
    system(qemu_img + " create -f qcow2 " + image + " " +  imagesize + "G")
    sys.exit(0)

def install(image, iso, memory, tap, cores):
    system(qemu_binary + "-cdrom " + iso + \
            " -boot order=d -drive file=" + image + ",format=qcow2" \
            + qemu_tap_pre + tap + qemu_tap_mid + tap + \
            qemu_tap_post + qemu_boiler + cores +
            " -m " + memory + "G -cpu host &")
    sys.exit(0)

def start(image, memory, tap, cores):
    system(qemu_binary + "-drive file=" + image + \
            ",format=qcow2" + qemu_tap_pre + tap +  \
            qemu_tap_mid + tap + qemu_tap_post + \
            qemu_boiler + cores + " -m " + memory + "G -cpu host &")
    sys.exit(0)

def start_no_image(iso, memory, tap, cores):
    system(qemu_binary + "-cdrom " + image + \
            " -boot order=d" + qemu_tap_pre + tap +  \
            qemu_tap_mid + tap + qemu_tap_post + qemu_boiler \
            + cores + " -m " + memory + "G -cpu host &")
    sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Qemu helper. Requires one of --create, --install, --start.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--create', action='store_true', help='Create a new qemu image')
    group.add_argument('--install', action='store_true', help='Install an iso onto a qemu image')
    group.add_argument('--start', action='store_true', help='Start an existing qemu image')
    parser.add_argument('--image', type=str, help='Qemu image.')
    parser.add_argument('--image-size', dest='imagesize', type=str, help='Specify image size for creation.')
    parser.add_argument('--iso', type=str, help='ISO Image to load from.')
    parser.add_argument('--memory', type=str, help='Amount of memory in G to load image with. [--memory=4]')
    parser.add_argument('--tap', type=str, help='Which tap to start image with. [--tap=3]')
    parser.add_argument('--cores', type=str, help='Number of cores to load image with. [--cores=2]')

    parser.set_defaults(memory='4', cores='2', tap='1', create=False, install=False, start=False)

    args = parser.parse_args()

    if args.create:
        if not args.image or not args.imagesize:
            print('Need to specify image name and image size.')
            sys.exit(0)
        create(args.image, args.imagesize)
    if args.install:
        if not args.image or not args.iso:
            print('Need to specify image name and ISO.')
            sys.exit(0)
        install(args.image, args.iso, args.memory, args.tap, args.cores)
    if args.start:
        if not args.image and not args.iso:
            print('Need to specify image name or iso if starting without an image.')
            sys.exit(0)
        elif args.image and not args.iso:
            start(args.image, args.memory, args.tap, args.cores)
        elif args.iso and not args.image:
            start_no_image(args.iso, args.memory, args.tap, args.cores)
