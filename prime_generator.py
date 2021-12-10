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
import math

def naive_prime_finder( n = 1000 ):
    primes = [2] 
    isPrime = True
    i = 3
    while i < n:
        for j in range(2, int( math.sqrt(i) )+1 ):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        isPrime = True
        i += 2
    return primes

def prime_finder_2_0( n = 1000 ):
    primes = [2]
    isPrime = True
    i = 3
    while i <= n:
        checkLimit = int( math.sqrt(i)+1 )
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
        checkLimit = int( math.sqrt(i)+1 )
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

def prime_finder_2_2( n = 1000):
    def check_multiplicity(i, threes, fives):
        while i == threes or i == fives:
            if i == threes and i == fives:
                threes += 6
                fives += 10
                i += 2
            elif i == threes and i != fives:
                threes += 6
                i += 2
            elif i != threes and i == fives:
                i += 2
                fives += 10
        return i, threes, fives
    threes = 9
    fives = 15
    primes = [2]
    isPrime = True
    i = 3
    while i <= n-2:
        if i == threes or i == fives:
            i, threes, fives = check_multiplicity(i, threes, fives)
        checkLimit = int( math.sqrt(i) + 1 )
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
    sizes_to_measure = [50000,100000,150000,200000,300000,400000,500000]
    naive_times = []
    version_2_0_times = []
    version_2_1_times = []
    version_2_2_times = []
    for i in sizes_to_measure:
        # Get naive finder times and add to list
        if i <= 200000:
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
        # Get version 2.2 finders times and add to list
        startTime = time.time()
        prime_finder_2_2(i)
        endTime = time.time()
        version_2_2_times.append(endTime - startTime )
    # Plot results
    plt.plot( sizes_to_measure[:len(naive_times)], naive_times, marker = 'o', label = 'Naive Times' )
    plt.plot( sizes_to_measure, version_2_0_times, marker = 'o', label = 'My Version #1' )
    plt.plot( sizes_to_measure, version_2_1_times, marker = 'o', label = 'My Version #2')
    plt.plot( sizes_to_measure, version_2_2_times, marker = 'o', label = 'My Version #3')
    # Format graph
    plt.title('Prime Number Generator Times')
    plt.legend(['Naive Times', 'My Version #1', 'My Version #2', 'My Version #3'])
    plt.xlabel('Range to check')
    plt.ylabel('Time to find primes in range')
    plt.show()

if __name__ == '__main__':
    create_performace_reports()
    #prime_finder_2_2(1000)
    """
    startTime = time.time()
    print(prime_finder_2_1(10000000)[-1])
    endTime = time.time()
    print(endTime-startTime)
    """
    pass