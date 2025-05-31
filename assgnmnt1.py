a = [0, 1, -2, 3, -4, 5]
maxsum = 0
for i in range(0, len(a)):
    for j in range(i, len(a)):
        sumsubarray = 0
        for k in range(i, j + 1):
            sumsubarray += a[k]
        maxsum = max(maxsum, sumsubarray)
print(maxsum)


import random
numberofhits = 0
x = []
for i in range(1000000):
    x.append(random.uniform(-1, 1))
y = []
for j in range(1000000):
    y.append(random.uniform(-1, 1))
for k in range(1000000):
    if x[k]**2 + y[k]**2 <=1:
        numberofhits += 1
estimationofpi = 4 * numberofhits / 1000000
print(estimationofpi)


#BENIM CALISMALARIM
def fibonacci(n):
    array=[1,1]
    if n==0:
        return 0
    else:
        while n > 2:
            array.append(sum(array[-2:]))
            n= n-1
    return array[-1]
print(fibonacci(10))

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)
print(recursive_fibonacci(10))