#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

## compute the number of ring automorphism of M_k(F_{p^l})
def aut_matrix(p,k,l):
    res = l*p**(l*(k-1))
    if k > 1:
        for i in range(k-1):
            res = res * (p**(l*k)-p**(l*i))
    return res

## generate partition of n 
## a much better code than what I could ever write
## see https://jeromekelleher.net/generating-integer-partitions.html
def partition(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(a[: k + 2])
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(a[: k + 1])

## get the square root of the non-one square divisor of p
def divisors(p):
    if p == 1:
        yield 1
    sqrt=int(np.sqrt(p)+1)
    divisors_bigger_than_sqrt=[]
    for i in range(2,sqrt):
        if p % i == 0:
            sqrti = np.sqrt(i)
            if int(sqrti) == sqrti:
                yield int(sqrti)
            if i+1 != sqrt:
                divisors_bigger_than_sqrt.append(int(p/i))
    for i in reversed(divisors_bigger_than_sqrt):
        sqrti = np.sqrt(i)
        if int(sqrti) == sqrti:
            yield int(sqrti)
    sqrtp = np.sqrt(p)
    if int(sqrtp) == sqrtp:    
        yield int(sqrtp)

## get a non-one divisor for each p in P
def iterate_divisors(P):
    if len(P) == 1:
        for d in divisors(P[0]):
            yield (d,)
    else:
        for d in divisors(P[0]):
            for PP in iterate_divisors(P[1:]):
                yield (d,)+PP

## put everything in a set to avoid counting multiple times the same decomposition
def set_decompositions(P):
    return set([tuple(sorted([(P[i],D[i]) for i in range(len(P))])) for D in iterate_divisors(P)])

## def the factorial
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

## define the multiplicity of a decomposition
def mult(D):
    res = 1
    mult = 1
    for i in range(len(D)-1):
        if D[i] == D[i+1]:
            mult += 1
        else:
            res = res * factorial(mult)
            mult = 1
    return res

## compute the order of the automorphism group of the decomposition
def aut(D,p):
    res = mult(D)
    for (m,k) in D:
        res = res * aut_matrix(p,k,int(m/(k**2)))
    return res

## compute a(p^n)
def a(p,n):
    fn = factorial(p**n)
    res = fn
    for P in partition(n):
        if P[-1] == 1:
            continue        ## if all ones, we get a commutative ring
        decompositions = set_decompositions(P)
        for D in decompositions:
            res += int(fn/aut(D,p))
    return res
