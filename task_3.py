"""
Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

nums = []
n = 600851475143
for i in range(2, 10000):
    if n % i == 0:
        nums.append(i)

print(nums[-1])
