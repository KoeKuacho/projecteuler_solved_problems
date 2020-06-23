"""
Problem 16: Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

p = 1000
sum_digit_power = sum(list(map(int, str(2 ** p))))
print('result =', sum_digit_power)




