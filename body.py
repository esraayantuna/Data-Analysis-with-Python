class Body:
    # Construct a new Body object whose position is specified by
    # Vector object r, whose velocity is specified by Vector object
    # v, and whose mass is specified by float mass.
    def __init__(self, r, v, mass):
        self.__r = r        # Position
        self.__v = v        # Velocity
        self.__mass = mass  # Mass

    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt.
    def move(self, f, dt):
        a = f.scale(1 / self.__mass)
        self.__v = self.__v + (a.scale(dt))
        self.__r = self.__r + self.__v.scale(dt)

    # Return the force between Body objects self and other.
    def forceFrom(self, other):
        G = 6.67e-11
        delta = other.__r - self.__r
        dist = abs(delta)

        # Calculate the magnitude and the direction of the force.
        magnitude = (G * self.__mass * other.__mass) / (dist * dist)
        deltaDirection = delta.scale(1.0 / abs(delta))

        return deltaDirection.scale(magnitude)

    def __str__(self):
        s = "r = " + str(self.__r) + ", v = " + str(self.__v) + ", mass = " + str(self.__mass)
        return s