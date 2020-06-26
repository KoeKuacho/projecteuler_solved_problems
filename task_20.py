"""
Problem 20: Factorial digit sum
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


fact_100 = factorial(100)
total = 0
for i in str(fact_100):
    total += int(i)

print('Result =', total)
