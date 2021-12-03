#!python
"""
Prime Number Generator
11/29/2021 Henry Hall
henrydhall3.14@gmail.com
Dependencies:
"""

from pathlib import Path
import shelve

def naive_prime_finder( n = 1000 ):
    primes = [2]
    isPrime = True
    for i in range(3,n+1):
        for j in range(2, int( (i-1/2) ) ):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        isPrime = True
    return primes

def prime_finder_2_0( n = 1000 ):
    primes = [2]
    isPrime = True
    i = 3
    while i <= n:
        checkLimit = (i/2) + 1
        for j in primes:
            if j > checkLimit:
                break
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        isPrime = True
        i += 2
    return primes

def prime_finder_2_1( n = 1000):
    threes = 9
    primes = [2]
    isPrime = True
    i = 3
    while i <= n:
        checkLimit = (i/2) + 1
        if i == threes:
            isPrime = False
            threes += 6
        else:
            for j in primes:
                if j > checkLimit:
                    break
                if i % j == 0:
                    isPrime = False
                    break
        if isPrime:
            primes.append(i)
        isPrime = True
        i += 2
    return primes

if __name__ == '__main__':
    assert prime_finder_2_0() == prime_finder_2_1()
    pass