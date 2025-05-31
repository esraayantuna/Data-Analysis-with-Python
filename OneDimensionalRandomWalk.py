import random

def startRandomWalk(numRandoMWalks, minNumSteps, maxNumSteps, stepIncrement):
    maxNumDistinctSteps = ((maxNumSteps - minNumSteps) // stepIncrement) + 1
    returned = [0] * maxNumDistinctSteps
    radius = [0] * maxNumDistinctSteps
    randomWalkStepIndex = 0

    #   Simulate one dimensional random walk for a set of number of steps
    # 	starting from a given minimum value to a given maximum value.  The
    # 	range is traversed by incrementing the number of steps by a given
    # 	increment value.
    #
    # 	Each walk will be repeated a number of times (numberOfRandomWalks)
    # 	to collect statistics.  Each walk's statistics will be referenced
    # 	by the index "randomWalkStepIndex".
    for t in range (minNumSteps, maxNumSteps + stepIncrement, stepIncrement):
        returned[randomWalkStepIndex] = 0
        radius[randomWalkStepIndex] = 0

        for j in range (0, numRandoMWalks):
            # particle starts from the origin
            position = 0

            # Simulate t steps of random walk
            position = simulateRandomWalk(position, t)

            # If particle returns to the original, increment the counter for it
            if position == 0:
                returned[randomWalkStepIndex] += 1

            # Increment the sum of square of distance from the origin for the current random walk
            radius[randomWalkStepIndex] += (position * position)

        # Calculate the average of the square of the distance from the origin at the end of t steps.
        radius[randomWalkStepIndex] /= numRandoMWalks

        # Now increment the index for the next set of random walks for a different number of steps
        randomWalkStepIndex += 1

    return randomWalkStepIndex, radius, returned


# This function simulates a one-dimensional random walk of t steps
# on a particle with a given initial position and returns the position
# after t steps
def simulateRandomWalk(position, t):
    # Each random walk will consist of t steps
    for i in range (0, t):
        # Throw a random number between 0 and 1
        randomDraw = random.uniform(0.0, 1.0)
        if randomDraw < 0.5:
            position += 1
        else:
            position -= 1

    return position


# This program must be run as follows:
# 
# 			startRandomWalk(N, min, max, step)
# 
# where N is the number of random walks for a given number of steps,
# min is the minimum number of steps you want to simulate,
# max is the maximum number of steps you want to simulate,
# and step is the increment in number of steps.
#
# For instance, if you want to simulate random walks of steps 100, 200, 300, 
# 400, and 500, each to be repeated 2000 times, you need to invoke this program 
# as follows:
# 
# 			startRandomWalk(2000, 100, 500, 100)
# 
numRandoMWalks = 2000
minNumSteps = 100
maxNumSteps = 500
stepIncrement = 100
N, radius, returnedToOrigin = startRandomWalk(numRandoMWalks, minNumSteps, maxNumSteps, stepIncrement)

# Print out the number of times a particle returned to the origin.
print("# Number of steps vs percentage of times that the particle returns to the origin\n")
for i in range (0, N):
    print(minNumSteps + i * stepIncrement, 100.0 * returnedToOrigin[i] / numRandoMWalks)

# Print out the average of the square of the distance from the origin.
print("\n\n# Number of steps vs average of square of distance from origin\n")
for i in range (0, N):
    print(minNumSteps + i * stepIncrement, radius[i])