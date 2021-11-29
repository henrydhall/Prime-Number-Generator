#!python
"""
Prime Number Generator
11/29/2021 Henry Hall
henrydhall3.14@gmail.com
Dependencies:
"""

from pathlib import Path

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
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        isPrime = True
        i += 2
    return primes

if __name__ == '__main__':
    print(naive_prime_finder(100000))
    #print(3%2)
    #assert naive_prime_finder(1000) == prime_finder_2_0(1000)
    #print(prime_finder_2_0(100000))
    pass