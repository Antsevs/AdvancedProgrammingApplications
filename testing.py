import math
import cmath

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "1.2":
        closeVal = False

        x = 24*(math.pi/180) #convert x to radians
        y = 0.4
        f = (2*math.cos(5*math.pi*x)*math.sin(6*y))/(2*math.sqrt(math.cos(math.sin(3*x+y)))+4*math.log(math.cos(y)))
        fStr = str(f) #Convert all calculated floats to str for printing
        xStr = str(x)
        yStr = str(y)
        print("input x = " + xStr)
        print("input y = " + yStr)
        print("f(x,y) = " + fStr)
    elif choice == "1.6":
        closeVal = False

        R = float(input('Enter annual interest rate as a percent: '))/12 #prompt user for needed info
        N = int(input('Enter the number of years for the mortgage: '))*12
        L = float(input('Enter the initial loan amount: '))
        P = (R*L)/(1-(1+R)**(-N)) #calculation
        print('Your monthly mortgage payment is: {}'.format(P)) #format p for concactenation and print
    elif choice == "1.7":
        closeVal = False

        r = float(input('Please enter the value for a resistor: ')) #Prompt user for RLC data
        l = float(input('Please enter the value for an inductor: '))
        c = float(input('Please enter the value for a capacitor: '))

        #series circuit calculations ----------------
        
        neperS = r/(2*l)
        resS = 1/(math.sqrt(l*c))
        rootsS1 = -neperS + cmath.sqrt(neperS**(2)-resS**(2))
        rootsS2 = -neperS - cmath.sqrt(neperS**(2)-resS**(2))

        #parallel circuit calculations ---------------
        
        neperP = 1/(2*r*c)
        resP = 1/(math.sqrt(l*c))
        rootsP1 = -neperP + cmath.sqrt(neperP**(2)-resP**(2))
        rootsP2 = -neperP - cmath.sqrt(neperP**(2)-resP**(2))
        
        print('Series Neper Frequency: ', neperS, '\nParallel Neper Frequency: ', neperP)
        print('Series Resonant Frequency: ', resS, '\nParallel Resonant Frequency: ', resP)
        print('Series root 1: ', rootsS1, '\nSeries root 2: ', rootsS2)
        print('Parallel root 1: ', rootsP1, '\nParallel root 2: ', rootsP2)
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (1.2, 1.6, or 1.7)\nor type 'exit' to close the program\n")
    menu(choice)
