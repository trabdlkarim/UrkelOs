#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:21:22 2019

@author: trabdlkarim
"""
import sys
import argparse as ap

def find_sum_of_mul(limit):
    total = 0
    for i in range(limit):
        if i%3 == 0 or i%5 ==0:
            total += i
    return total


def main(argv):
    parser = ap.ArgumentParser(description="Finds the sum of the multiples of 3 or 5 below a limit")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--limit",nargs=1,type=int,metavar="N",help="determines the limit ")
    group.add_argument("integer",nargs='?',type=int, default=100,metavar="N",help="determine also the limit as -l option")
    args = parser.parse_args(sys.argv[1:])
    if args.limit:
        limit = args.limit[0]
    else:
        limit=args.integer
    total = find_sum_of_mul(limit)     
    print("sum of multiples of 3 or 5 below  %i is %i " % (limit,total))
    
if __name__=="__main__":
    main(sys.argv)
    