"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

start = time.time()

i = 10
count_divider = False

while count_divider is False:
    for n in range(3, 20):
        if i % n == 0:
            count_divider = True
            continue
        else:
            count_divider = False
            break
    i += 10

print('Result =', i - 10)

end = time.time()
print('Time of execution = ' + str(end - start))
