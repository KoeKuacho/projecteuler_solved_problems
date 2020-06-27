"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

a = range(1, 1000)
b = range(1, 1000)

mul = []
palyndroms = []

for i in a:
    for x in b:
        mul.append(i * x)

for num in mul:
    if str(num) == str(num)[::-1]:
        palyndroms.append(num)

print('Result =', max(palyndroms))