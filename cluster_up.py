#!/usr/bin/python
from os import system
import sys
import argparse
from qemu import create_tap, start

systems = ['k8-master', 'k8-node0', 'k8-node1', 'k8-node2',]
taps = ['0', '1', '2', '3',]

def tap_build():
    for x in range(len(systems)):
        print('creating tap', taps[x])
        try:
            create_tap(taps[x], 'eno1')
        except:
            continue

def cluster_build():
    for x in range(len(systems)):
        try:
            start(systems[x], '4', taps[x], '2')
        except:
            continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brings up k8s cluster and taps, takes as argument either --start or --taps')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--taps', action='store_true', help='Create taps for cluster')
    group.add_argument('--start', action='store_true', help='Starts cluster systems')

    parser.set_defaults(create=False, taps=False)

    args = parser.parse_args()
    if args.taps: tap_build()
    if args.start: cluster_build()
