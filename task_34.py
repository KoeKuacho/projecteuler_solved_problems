"""
Problem 34: Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


total = 0
sum_factorial = 0
for i in range(3, 1000000):
    for j in str(i):
        sum_factorial += factorial(int(j))
    if sum_factorial == i:
        total += i
    sum_factorial = 0

print('Result =', total)
