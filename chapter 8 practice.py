import math
import cmath
import matplotlib.pyplot as plt
import numpy


x = numpy.arange(-10, 10, 0.1)
        fx = (x**5)+(3*x**4)+(2*x**3)+(10*x**2)+(6*x)+10

        plt.plot(x,fx, 'g--')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('f(x) = x^5+3x^4+2x^3+10x^2+6x+10')
        plt.axis([-10, 10, min(fx), max(fx)])
        plt.legend(['f(x)'])
        plt.grid(True)
        plt.show()
