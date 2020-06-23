"""
Problem 16: Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

n = 100000
d_d = sum(list(map(int, str(2**n))))
print(d_d)


