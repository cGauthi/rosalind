#!/usr/bin/env python3

k = int(input("How many homozygous dominant organisms are present? "))
m = int(input("Heterozygous? "))
n = int(input("Homozygous recessive? "))

p = k + m + n
q = (p-1)

def domcross():
    d = ((k/p)*(k-1)/q) + ((k/p)*(m/q)) + ((k/p)*(n/q)) + ((m/p)*(k/q)) + ((n/p)*(k/q))
    return d

def heterocross():
    h = ((m/p)*(m-1)/q)
    return h

def heterorecross():
    x = ((m/p)*(n/q)) + ((n/p)*(m/q))
    return x

prob = domcross() + .75*heterocross() + .5*heterorecross()

print("Total Population:", p)
print("Probability of dominant phenotype:", prob)
