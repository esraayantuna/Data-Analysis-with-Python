import math
from turtle import Turtle, Screen
import drawpolygon

#
# Draws one triangle with bottom vertex at coordinate (x, y) and side length of s.
#
# Then, recursively calls itself three times to generate the next set of Sierpinski
# triangles to the left, to the right, and above the current triangle you just drew.
# Here the parameters are:
# t: Turtle Graphics object for drawing
# n: the number of recursive iterations
# x, y: the coordinates of the vertex of the equilateral filled triangle with side
#       length of s to be drawn pointing down.
def sierpinski(t, n, x, y, length):
    if n == 0:
        return

    # Draw a filled triangle pointing down with the following
    # coordinates as vertices
    height = length * math.sqrt(3) / 2
    x1 = x - length / 2
    x2 = x + length / 2
    y1 = y + height
    xCoors = [x, x1, x2]
    yCoors = [y, y1, y1]
    drawpolygon.draw_filled_triangle(t, xCoors, yCoors)

    # Next, recursively draw filled equilateral triangles to the left, to the right,
    # and above the triangle drawn above.  The side length of these equilateral
    # triangles will be half the length of that of the equilateral triangle above.
    halfBase = math.sqrt(length * length - height * height)
    x0 = x - halfBase
    x1 = x + halfBase
    sierpinski(t, n - 1, x0, y, length / 2)
    sierpinski(t, n - 1, x1, y, length / 2)
    sierpinski(t, n - 1, x, y + height, length / 2)

def main():
    n = int(input("Number of iterations: "))

    t = Turtle('turtle')
    screen = t.getscreen()
    screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
    t.hideturtle()

    # Draw the main unfilled equilateral triangle.
    # Each side of this triangle will be equal to 1 (normalized depending on your screen resolution).
    # See the first figure in the assignment sheet.
    xCoors = [0, 1.0, 0.5]
    yCoors = [0, 0, math.sqrt(3) / 2]
    drawpolygon.draw_triangle(t, xCoors, yCoors)

    # The x and y coordinates of the vertex of the triangle that will point
    # downwards.  See the filled triangle in the first figure in the assignment
    # sheet.
    xi = 0.5
    yi= 0
    side_length = 1.0
    sierpinski(t, n, xi, yi, side_length/2)

    # This will make sure your graph will be up until you close it.
    screen.exitonclick()

main()