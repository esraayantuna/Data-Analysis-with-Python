class ComplexNumber:
    def __init__(self, re=0, im=0):
        self.real = re
        self.imaginary = im

    def add(self, z):
        sum = ComplexNumber()
        sum.real = self.real + z.real
        sum.imaginary = self.imaginary + z.imaginary
        return sum

    def subtract(self, z):
        diff = ComplexNumber()
        diff.real = self.real - z.real
        diff.imaginary = self.imaginary - z.imaginary
        return diff

    def multiply(self, z):
        product = ComplexNumber()
        # exercise: implement complex number product
        return product

    def __str__(self):
        if self.imaginary > 0:
            s = "(" + str(self.real) + " + " + str(self.imaginary) + "i)"
        elif self.imaginary < 0:
            s = "(" + str(self.real) + " - " + str(-self.imaginary) + "i)"
        else:
            s = "(" + str(self.real) + ")"
        return s