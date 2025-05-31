# Calculates the position and velocity as a function of time.
def oneDimensionalMotion(numTimeSteps, position, velocity, timeStep, k, m):
    g = 9.8
    i = 0
    while i < numTimeSteps and (position + timeStep * velocity) > 0:
        # Calculate the next position.
        position = position + timeStep * velocity
        # Calculate the next velocity,
        # Force is equal to (-mg - kv^2)
        velocity = velocity + timeStep * (-g) + timeStep * (-k / m) * velocity * velocity

        # Print out the position and velocity as a function of time.
        print(timeStep * (i + 1), ",", position,  ",", velocity)
        i += 1

    return position, velocity

# assume a small spherical metal ball with mass 100 grams
m = 0.1

# assume some overall small constant to model air resistance
k = 0.0002

simSteps = 1000
position = 100
velocity = 0
time = 2
timeStep = time / simSteps

print("Initial Position=", position, "Initial Velocity=", velocity)
finalPos, finalVelocity = oneDimensionalMotion(simSteps, position, velocity, timeStep, k, m)
print("Final Position=", finalPos, "Final Velocity=", finalVelocity)
