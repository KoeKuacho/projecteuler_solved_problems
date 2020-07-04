"""
Problem 50: Consecutive prime sum
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import time

start = time.time()

n = 1000000
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0

primes = []
i = 2
while i <= n:
    if a[i] != 0:
        primes.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    i += 1

equal_numbers = []
check_sum = 0
for p in range(len(primes)):
    for j in range(0, p+1):
        check_sum += primes[j]
    if check_sum in primes and check_sum not in equal_numbers:
        equal_numbers.append(check_sum)
    check_sum = 0

print(equal_numbers)
print('Result =', equal_numbers[-1])

# print(primes)
# print(len(primes))

end = time.time()
print('Time of execution = ' + str(end - start))
