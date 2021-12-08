# Prime-Number-Generator
Efficient prime number generator to make a list of prime numbers.

# The Methods
* Naive
* My Versions, #1-3

# Time Comparisons
![Graph of Times of Methods](https://github.com/henrydhall/Prime-Number-Generator/tree/main/Figures)

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
    TODO: enter pseudocode for #3
                
