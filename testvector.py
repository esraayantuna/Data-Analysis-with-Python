from vector import Vector
def main():

    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(1.0, 2.0, 3.0)
    y = Vector(5.0, 2.0, 4.0)

    print('x        = ' + str(x))
    print('y        = ' + str(y))
    print('x + y    = ' + str(x + y))
    print('10x      = ' + str(x.scale(10.0)))
    print('|x|      = ' + str(abs(x)))
    print('<x, y>   = ' + str(x.dot(y)))
    print('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()
