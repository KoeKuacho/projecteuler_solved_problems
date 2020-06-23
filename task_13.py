"""
Problem #13: Large sum
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
with open('numbers.txt', 'r') as f:
    numbers = f.read().split('\n')
    sum_int_numbers = sum(list(map(int, numbers)))
    print(str(sum_int_numbers)[:10])
