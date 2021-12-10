# Prime-Number-Generator
Efficient prime number generator to make a list of prime numbers.

Test to verify accuracy of all methods.

# The Methods
* Naive
* My Versions, #1-3

# Time Comparisons
![Graph of Times of Methods](https://github.com/henrydhall/Prime-Number-Generator/blob/main/Figures/Figure_1.png)

# Analysis
As expected the naive method gets bogged down the fastest. This is mostly due to checking too many numbers.

My methods' main improvement is not having to check every number between 2 and sqrt of the number. Reducing 
the set of numbers checked to just primes generated so far made it much faster.

Method #2 is slightly more efficient by checking 3 without doing modular division.

Method #3 is a major dissapointment, I would have thought eliminating multiples of 3 and 5 would improve it 
even more but I was wrong. I think I could find a way to fix it, but so far I haven't had the time or energy.

# Conclusions
The ability to generator all prime numbers between 2 and 1,000,000 is kind of cool to have. 
But, considering that RSA Encryption uses numbers with 1024, 2048, and even 4,096 bits, 
my numbers with 24 bits that take about 20 seconds to generator are pretty lame. I'm going to try to 
implement a more efficient method at some point and try to close that 1000 bit gap.

## Naive Approach
    NaivePrimeFinder:
        input: int n
        output: list of all prime numbers 2-n
        data structures:
            bool: isPrime
            int: i=3, j=2
            list: primes = [2]

        while i<n
            for all j<sqrt(i)
                if i % j == 0
                    isPrime = False
                    break
            if isPrime
                append i to primes
            isPrime = True
            i += 2
        return primes
            
## My Method #1
    Method #1:
        input: int n
        output: list of all prime numbers 2-n
        data structures:
            bool: isPrime
            int: i = 3, j, checklimit
            list: primes = [2]

        while i<n
            checklimit = sqrt(i)
            for all j in primes
                if j > checklimit
                    break
                if i%j == 0
                    isPrime = False
                    break
            if isPrime
                append i to primes
            isPrime = True
            i += 2
        return primes

## My Method #2
    Method #2:
        input: int n
        output: list of all prime numbers 2-n
        data structures:
            bool: isPrime
            int: i = 3, j, checklimit, threes = 9
            list: primes = [2]

        while i<n
            if i == threes
                threes += 6
                i += 2
            checklimit = sqrt(i)
            for all j in primes
                if j > checklimit
                    break
                if i%j == 0
                    isPrime = False
                    break
            if isPrime
                append i to primes
            isPrime = True
            i += 2
        return primes

## My Method #3
    Method #3:
        input: int n
        output: list of all prime numbers 2-n
        data structures:
            functions: multiplicity_checker.
            bool: isPrime
            int: i = 3, j, checklimit, threes = 9, fives = 25
            list: primes = [2]
        
        multiplicity_checker:
            increment i, threes, fives, until i is not equal to either one.

        while i<n
            if i == threes or fives
                i, threes, fives = multiplicity_checker(i, three, fives)
            checklimit = sqrt(i)
            for all j in primes
                if j > checklimit
                    break
                if i%j == 0
                    isPrime = False
                    break
            if isPrime
                append i to primes
            isPrime = True
            i += 2
        return primes
                
