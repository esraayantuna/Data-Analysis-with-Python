import math

class Vector:
    def __init__(self, xcoor=0, ycoor=0, zcoor=0):
        self.__x = xcoor
        self.__y = ycoor
        self.__z = zcoor

    # The __add__() is a special method in Python that defines what happens
    # when you add two objects with the + operator.
    #
    # When you call v1 + v2, under the hood you are calling v1.__add__(v2)
    def __add__(self, v):
        sum = Vector()
        sum.__x = self.__x + v.__x
        sum.__y = self.__y + v.__y
        sum.__z = self.__z + v.__z
        return sum

    # The __sub__() is a special method in Python that defines what happens
    # when you subtract one object from another with the - operator.
    #
    # When you call v1 - v2, under the hood you are calling v1.__sub__(v2)
    def __sub__(self, v):
        diff = Vector()
        diff.__x = self.__x - v.__x
        diff.__y = self.__y - v.__y
        diff.__z = self.__z - v.__z
        return diff

    def __abs__(self):
        return math.sqrt(self.dot(self))

    def scale(self, c):
        newV = Vector(c * self.__x, c * self.__y, c * self.__z)
        return newV

    def dot(self, v):
        product = 0
        product += self.__x * v.__x
        product += self.__y * v.__y
        product += self.__z * v.__z
        return product

    def __str__(self):
        s = "(" + str(self.__x) + ", " + str(self.__y) + ", " + str(self.__z) + ")"
        return s
