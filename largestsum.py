import math
import random

'''
Given an integer array, find its contiguous subarray with maximum sum.
Input: An array of 𝑛 integer numbers (𝑎[0],…,𝑎[𝑛−1])
Output: The maximum value of the sum 𝑎[𝑙] +⋯+ 𝑎[𝑟] among all possible intervals [𝑙,𝑟] with 0 <= 𝑙<=𝑟<=𝑛−1.

Note that the brute force way is to calculate the following sums and keep track of the max is as follows:
a[0]
a[0] + a[1]
a[0] + a[1] + a[2]
...
a[0] + a[1] + ... + a[n-1]

a[1]
a[1] + a[2] 
a[1] + a[2] + a[3]
...
a[1] + ... + a[n-1]

a[2]
a[2] + a[3]
a[2] + a[3] + ... + a[n-1]

...
a[n-1]
'''

def max_sum(a):
    current_max = float('-inf')
    current_max_range = []
    n = len(a)
    for l in range (0, n):
        for r in range (0, n):
            sum = 0
            max_range = []
            for k in range(l,r + 1):
                max_range.append(k)
                sum += a[k]

            if sum > current_max:
                current_max = sum
                current_max_range = max_range

    return current_max, current_max_range

N = 10
a= []
for i in range (0, N):
    num = random.randint(-100, 100)
    a.append(num)

print(a)
maxsum, maxsumrange = max_sum(a)
print ("max sum is ", maxsum)
print ("The range is:")
print(maxsumrange)

'''
Output from one of my tests:

[-96, 99, -12, 48, -26, -6, -19, -44, -99, 42]
max sum is  135
The range is:
[1, 2, 3]
'''