# Prime-Number-Generator
Efficient prime number generator to make a list of prime numbers.

# The Methods
* Naive
* My Versions, #1-3

## Naive
NaivePrimeFinder:
    input: int n
    output: list of all prime numbers 2-n

    for all i\<n
        for all j\<sqrt(i)
            if i % j == 0
                i is not prime
                break
        if i is prime, append it to list of prime numbers
    return list of prime numbers
            