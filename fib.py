#!/usr/bin/python

#check if number is a fibonnaci one

def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

for i in range(20):
    print fibi(i)
