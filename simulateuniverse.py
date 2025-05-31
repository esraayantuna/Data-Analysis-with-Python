from universe import Universe
import time

def main():
    # Number of gravitational bodies
    n = 10

    # Number of steps
    K = 1000

    # Simulation time step.
    dt = 20000
    universe = Universe(n)
    print("Initial universe:\n" + str(universe))

    time.time_ns()
    # Simulate the dynamics of this mini universe
    for i in range(K):
        universe.increaseTime(dt)

    print("Universe after " + str(K) + " steps of simulation:\n" + str(universe))

if __name__ == '__main__':
    main()

