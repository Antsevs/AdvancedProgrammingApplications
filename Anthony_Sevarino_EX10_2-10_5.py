import math
import cmath
import numpy
from scipy.misc import derivative
from scipy.integrate import quad, romberg

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "10.2":
        closeVal = False

        x1, y1, x2, y2 = [float(x) for x in input('Please enter the two pairs of final data points, separated by a comma \n(i.e. 1, 2, 3, 4): ').split(',')]
        x3 = float(input('Please enter the x value of the extrapolated y: '))
        y3 = y1 + ((x3-x1)/(x2-x1))*(y2-y1)
        print('The extrapolated value of y is {}.'.format(y3))
        
    elif choice == "10.3":
        closeVal = False

        #repeat of 10.2
        x1, y1, x2, y2 = [float(x) for x in input('Please enter the two pairs of final data points, separated by a comma \n(i.e. 1, 2, 3, 4): ').split(',')]
        x3 = float(input('Please enter the x value of the extrapolated y: '))
        y3 = y1 + ((x3-x1)/(x2-x1))*(y2-y1)
        print('The extrapolated value of y is {}.'.format(y3))

        x = numpy.array([x1, x2, x3])
        y = numpy.array([y1, y2, y3])
        
        degree = 4
        fx = []
        #create polynomials of degrees 4 to 9 depending on x3 and y3
        for i in range (4,9):
            z = numpy.polyfit(x, y, deg = degree)
            fx.append(numpy.poly1d(z))
            degree += 1

        print('{}\t||\t{}\t||\t{}\t||\t{}\t||\t{}\t||\t{}\t||{}\t||\t{}\n'.format(x3, y3, z(1), z(2), z(3), z(4), z(5), z(6)))

        
        
    elif choice == "10.4":
        closeVal = False

        def f(x):
            return x**3+2*x**2+9*numpy.cos(5*x)

        D1 = derivative(f, 2.8, dx = 1e-3)
        D2 = derivative(f, 2.8, dx = 1e-3, n = 2)
        D3 = derivative(f, 2.8, dx = 1e-3, n = 3, order = 5)
        print('First Derivative: {}\nSecond Derivative: {}\nThird Derivative: {}'.format(D1, D2, D3))
        
    elif choice == "10.5":
        closeVal = False
        
        dvdt = lambda x: (2*numpy.cos(x)*numpy.sin(2*x))/10e-6

        v = romberg(dvdt, 0.001, 0.002)

        print(v)
        
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (10.2, 10.3, 10.4, or 10.5)\nor type 'exit' to close the program\n")
    menu(choice)
