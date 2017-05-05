#!/usr/bin/env python3

n = 33
k = 3

def rabbits(n):
    if (n == 0):
        p = 0;
    elif (n == 1):
        p = 1;
    else:
        p = rabbits(n-1) + k*rabbits(n-2);
    return p;

pairs = rabbits(n)
print(pairs)
