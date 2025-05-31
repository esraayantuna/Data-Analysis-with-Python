import math
from turtle import Turtle, Screen
import drawpolygon

def sierpinski(t, n, x, y, s):

    xCoors=[x,x-(s/2), x+(s/2)]
    yCoors=[y,y+(s*(math.sqrt(3)/2)),y+(s*(math.sqrt(3)/2))]
    drawpolygon.draw_filled_triangle(t, xCoors, yCoors)

    if n > 1:
        sierpinski(t,n-1, x-(s/2) ,y,s/2)
        sierpinski(t,n-1, x+(s/2), y, s/2)
        sierpinski(t,n-1, x, y+math.sqrt(3)*(s/2) , s/2)

def main():
    n = int(input("Number of iterations: "))

    t = Turtle('turtle')
    screen = t.getscreen()
    screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
    t.hideturtle()

    xCoors = [0, 1.0, 0.5]
    yCoors = [0, 0, math.sqrt(3) / 2]
    drawpolygon.draw_triangle(t, xCoors, yCoors)

    xi = 0.5
    yi= 0
    side_length = 1.0
    sierpinski(t, n, xi, yi, side_length/2)

    screen.exitonclick()

main()