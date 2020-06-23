"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import sqrt

n = 2000000
primes = []
for i in range(2, n + 1):
    for j in primes:
        if j > int((sqrt(i)) + 1):
            primes.append(i)
            break
        if (i % j == 0):
            break
    else:
        primes.append(i)
print(sum(primes))