#!python
"""
Prime Number Generator
11/29/2021 Henry Hall
henrydhall3.14@gmail.com
Dependencies:
"""

from pathlib import Path
import shelve
import time
from matplotlib import pyplot as plt

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
    while i <= n-2:
        if i == threes:
            threes += 6
            i += 2
        checkLimit = int( (i/2) + 1 )
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

def create_performace_reports():
    sizes_to_measure = [100,1000,5000,7500,10000,20000,40000]
    naive_times = []
    version_2_0_times = []
    version_2_1_times = []
    for i in sizes_to_measure:
        # Get naive finder times and add to list
        if i < 20000:                 # Bogs down at about 50k
            startTime = time.time()
            naive_prime_finder(i)
            endTime = time.time()
            naive_times.append( endTime - startTime )
        # Get version 2.0 finders times and add to list
        startTime = time.time()
        prime_finder_2_0(i)
        endTime = time.time()
        version_2_0_times.append( endTime - startTime )
        # Get version 2.1 finders times and add to list
        startTime = time.time()
        prime_finder_2_1(i)
        endTime = time.time()
        version_2_1_times.append( endTime - startTime )
        # Plot results
    plt.plot( sizes_to_measure[:len(naive_times)], naive_times, marker = 'o' )
    plt.plot( sizes_to_measure, version_2_0_times, marker = 'o' )
    plt.plot( sizes_to_measure, version_2_1_times, marker = 'o' )
    plt.show()

if __name__ == '__main__':
    create_performace_reports()
    pass