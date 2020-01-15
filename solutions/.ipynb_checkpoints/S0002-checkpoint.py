#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:11:25 2019

@author: trabdlkarim
"""

def fibo(n):
    if n <2:
        return n
    else: 
        return fibo(n-1) + fibo(n-2)
    
def main():
    total=0
    for i in range(1,11):
        fib = fibo(i)
        if (fib & 1)==0:
            total += fib
    print(total)

if __name__=="__main__":
   main()
