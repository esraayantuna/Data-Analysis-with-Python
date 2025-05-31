from body import Body
from vector import Vector
from random import gauss

class Universe:
    # Construct a new Universe object by generating random positions,
    # velocities, and masses with the following mean and standard
    # deviation values to use in the random number generator.
    meanPosition = 3.5e10
    stdPosition  = 6.0e04

    meanVelocity = 1.4e04
    stdVelocity = 1.2e02

    meanMass = 3.0e28
    stdMass = 1.7e14

    def __init__(self, n):
        self.__bodies = []
        for i in range(n):
            # Randomly generate velocity, position, and mass
            r = Vector(gauss(Universe.meanPosition, Universe.stdPosition),
                       gauss(Universe.meanPosition, Universe.stdPosition),
                       gauss(Universe.meanPosition, Universe.stdPosition),)
            v = Vector(gauss(Universe.meanVelocity, Universe.stdVelocity),
                       gauss(Universe.meanVelocity, Universe.stdVelocity),
                       gauss(Universe.meanVelocity, Universe.stdVelocity),)
            mass = gauss(Universe.meanMass, Universe.stdMass)

            # Add to the list of bodies
            self.__bodies.append(Body(r, v, mass))

    # Simulate the passing of dt seconds in self.
    def increaseTime(self, dt):
        # Initialize the forces to zero.
        n = len(self.__bodies)
        f = [None] * n
        
        # Compute the forces.
        for i in range(n):
            f[i] = Vector()
            for j in range(n):
                if i != j:
                    bodyi = self.__bodies[i]
                    bodyj = self.__bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)

        # Move the bodies.
        for i in range(n):
            self.__bodies[i].move(f[i], dt)

    # Draw self to standard draw.
    def __str__(self):
        s = ""
        for i in range(len(self.__bodies)):
            s += "Particle (" + str(i) + ") " + str(self.__bodies[i]) + "\n"
        return s