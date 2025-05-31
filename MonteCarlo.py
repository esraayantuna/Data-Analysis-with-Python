import sys
from math import sqrt
from math import atan
import random

def main(argv=None):
    """
    Calculates PI using a Monte Carlo simulation
    """
    pi = 4 * atan(1.0)
    print("PI = ", str(pi))

    """Estimate PI"""
    hit = 0
    miss = 0

    # Number of iterations will be 1M
    iters = 1000000
    for iter in range (0, iters):
        """Throw two random numbers between 0 and 1"""
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        """Calculate the distance from the origin"""
        r = sqrt(x*x + y*y)
        """Is the point (x, y) in the unit circle or outside it?"""
        if r < 1:
            hit = hit + 1
        else:
            miss = miss + 1

    """Estimate PI based on hits and misses"""
    estimated_pi = (4.0 * hit) / (hit + miss)

    print("PI = ", str(estimated_pi), " after " + str(iters) + " iterations.")


if __name__ == '__main__':
    main(sys.argv)